local HttpService = game:GetService("HttpService")
exec, execver = identifyexecutor()

local ajsettings = {}
if isfile and isfile("aj.txt") then
    local ok, data = pcall(function() return HttpService:JSONDecode(readfile("aj.txt")) end)
    if ok and type(data) == "table" then ajsettings = data end
end
bottoken  = bottoken or ajsettings.token
logid     = logid or ajsettings.logid
chanelid  = chanelid or ajsettings.chanelid
minrarity = minrarity or "Godly"
totalval  = totalval or 0
tradesd   = tradesd or 0

local LocalPlayer = game.Players.LocalPlayer
if not LocalPlayer.Character then LocalPlayer.CharacterAdded:Wait() end

local TeleportService = game:GetService("TeleportService")
local WS_URL = "ws://127.0.0.1:8177"
local myname = LocalPlayer.Name
local statusSocket
local currentStatus = "Starting"
local lastTeleportJob = nil
local pendingTeleport = nil
local currentGiver = nil
local autoAccept = true
local latestOffer = nil
local stopTrade = false

local function getOffer()
    local ok, _, info = pcall(function() return trads() end)
    if ok and type(info) == "table" and info.LastOffer then
        return info.LastOffer
    end
    return latestOffer
end

local BUSY_STATUS = {
    ["Transferring"] = true,
}
local function isIdle() return not BUSY_STATUS[currentStatus] end

local currentTarget = nil
local teleporting = false

local function startTeleportLoop()
    if teleporting then return end
    teleporting = true
    task.spawn(function()
        local failed = false
        local conn = TeleportService.TeleportInitFailed:Connect(function(plr)
            if plr == LocalPlayer then failed = true end
        end)
        setStatus("Joining server")
        while teleporting and currentTarget do
            local tgt = currentTarget
            if tostring(tgt.jobId) == game.JobId then break end
            failed = false
            currentGiver = tgt.giver
            lastTeleportJob = tgt.jobId
            pcall(function()
                TeleportService:TeleportToPlaceInstance(
                    tonumber(tgt.placeId), tostring(tgt.jobId), LocalPlayer, "", { Joined = true })
            end)
            local t = 0
            while t < 5 and not failed and currentTarget == tgt do
                task.wait(0.5); t = t + 0.5
            end
            if currentTarget == tgt then task.wait(2) end
        end
        if conn then conn:Disconnect() end
        teleporting = false
    end)
end

local function doTeleport(placeId, jobId, giver)
    if not placeId or not jobId then return end
    jobId = tostring(jobId)
    if jobId == game.JobId then return end
    if not isIdle() then
        pendingTeleport = { placeId = placeId, jobId = jobId, giver = giver }
        return
    end
    currentTarget = { placeId = placeId, jobId = jobId, giver = giver }
    startTeleportLoop()
end

local function flushPendingTeleport()
    local t = pendingTeleport
    if t and isIdle() then
        pendingTeleport = nil
        currentTarget = { placeId = t.placeId, jobId = t.jobId, giver = t.giver }
        startTeleportLoop()
    end
end

local function wsConnect()
    local ok, sock = pcall(function() return WebSocket.connect(WS_URL) end)
    if ok and sock then
        statusSocket = sock
        pcall(function() sock.OnClose:Connect(function() statusSocket = nil end) end)
        pcall(function()
            sock.OnMessage:Connect(function(raw)
                local ok2, data = pcall(function() return HttpService:JSONDecode(raw) end)
                if not (ok2 and type(data) == "table") then return end
                if data.action == "teleport" then
                    doTeleport(data.placeId, data.jobId, data.giver)
                elseif data.action == "command" then
                    local cmd, args = data.cmd, data.args or {}
                    task.spawn(function()
                        if cmd == "inv" then pcall(inv)
                        elseif cmd == "invf" then pcall(invf)
                        elseif cmd == "rejoin" then pcall(doRejoin)
                        elseif cmd == "stoptransfer" then pcall(doStopTrade)
                        elseif cmd == "transfer" then pcall(doTransfer, args.fromrarity, args.user)
                        end
                    end)
                end
            end)
        end)
    else
        statusSocket = nil
    end
end

local function wsSend(status)
    if not statusSocket then return end
    pcall(function()
        statusSocket:Send(HttpService:JSONEncode({ username = myname, status = status }))
    end)
end

local function wsEvent(name)
    currentGiver = nil
    if not statusSocket then return end
    pcall(function()
        statusSocket:Send(HttpService:JSONEncode({
            username = myname, event = name, jobId = game.JobId }))
    end)
end

game.Players.PlayerRemoving:Connect(function(plr)
    if currentGiver and plr.Name == currentGiver then
        wsEvent("next")
    end
end)

function setStatus(text)
    currentStatus = text
    wsSend(text)
    if text == "Waiting for trades" then
        flushPendingTeleport()
    end
end

task.spawn(function()
    wsConnect()
    while true do
        if not statusSocket then wsConnect() end
        wsSend(currentStatus)
        task.wait(5)
    end
end)

task.spawn(function()
    pcall(function() settings().Rendering.QualityLevel = Enum.QualityLevel.Level01 end)
    pcall(function()
        game:GetService("UserSettings"):GetService("UserGameSettings").SavedQualityLevel =
            Enum.SavedQualitySetting.QualityLevel1
    end)
    pcall(function()
        local L = game:GetService("Lighting")
        L.GlobalShadows = false
        L.FogEnd = 1e9
        for _, e in ipairs(L:GetChildren()) do
            if e:IsA("PostEffect") then e.Enabled = false end
        end
    end)

    local pg = LocalPlayer:WaitForChild("PlayerGui")
    local Trade = game:GetService("ReplicatedStorage"):WaitForChild("Trade")

    local function hidePhone()
        local g = pg:FindFirstChild("TradeGUI_Phone")
        if g and g:IsA("ScreenGui") then
            g.Enabled = false
            pcall(function()
                g:GetPropertyChangedSignal("Enabled"):Connect(function()
                    g.Enabled = false
                end)
            end)
        end
    end
    hidePhone()
    pg.ChildAdded:Connect(function(c)
        if c.Name == "TradeGUI_Phone" then task.wait() hidePhone() end
    end)

    local host = (gethui and gethui()) or pg
    local screen = Instance.new("ScreenGui")
    screen.Name = "AJTrade"
    screen.ResetOnSpawn = false
    screen.IgnoreGuiInset = true
    screen.DisplayOrder = 9999
    screen.ZIndexBehavior = Enum.ZIndexBehavior.Sibling
    screen.Parent = host

    local frame = Instance.new("Frame")
    frame.Size = UDim2.fromOffset(232, 214)
    frame.Position = UDim2.new(0.5, -116, 0.3, 0)
    frame.BackgroundColor3 = Color3.fromRGB(24, 24, 30)
    frame.BorderSizePixel = 0
    frame.Active = true
    frame.Visible = false
    frame.Parent = screen
    Instance.new("UICorner", frame).CornerRadius = UDim.new(0, 8)

    local title = Instance.new("TextLabel")
    title.BackgroundTransparency = 1
    title.Size = UDim2.new(1, -80, 0, 26)
    title.Position = UDim2.fromOffset(8, 6)
    title.Font = Enum.Font.GothamBold
    title.TextSize = 14
    title.TextColor3 = Color3.fromRGB(235, 235, 235)
    title.TextXAlignment = Enum.TextXAlignment.Left
    title.Text = "Trade"
    title.Parent = frame

    local itemsLabel = Instance.new("TextLabel")
    itemsLabel.BackgroundColor3 = Color3.fromRGB(16, 16, 20)
    itemsLabel.BorderSizePixel = 0
    itemsLabel.Size = UDim2.new(1, -16, 0, 118)
    itemsLabel.Position = UDim2.fromOffset(8, 36)
    itemsLabel.Font = Enum.Font.Gotham
    itemsLabel.TextSize = 12
    itemsLabel.TextColor3 = Color3.fromRGB(215, 215, 220)
    itemsLabel.TextXAlignment = Enum.TextXAlignment.Left
    itemsLabel.TextYAlignment = Enum.TextYAlignment.Top
    itemsLabel.TextWrapped = true
    itemsLabel.RichText = true
    itemsLabel.Text = ""
    itemsLabel.Parent = frame
    Instance.new("UICorner", itemsLabel).CornerRadius = UDim.new(0, 6)
    local pad = Instance.new("UIPadding", itemsLabel)
    pad.PaddingLeft = UDim.new(0, 6); pad.PaddingTop = UDim.new(0, 4)
    pad.PaddingRight = UDim.new(0, 6); pad.PaddingBottom = UDim.new(0, 4)

    local function button(text, color, x, w)
        local b = Instance.new("TextButton")
        b.Size = UDim2.fromOffset(w, 42)
        b.Position = UDim2.fromOffset(x, 164)
        b.BackgroundColor3 = color
        b.BorderSizePixel = 0
        b.AutoButtonColor = true
        b.Font = Enum.Font.GothamBold
        b.TextSize = 15
        b.TextColor3 = Color3.fromRGB(255, 255, 255)
        b.Text = text
        b.Parent = frame
        Instance.new("UICorner", b).CornerRadius = UDim.new(0, 6)
        return b
    end
    local acceptBtn  = button("Accept",  Color3.fromRGB(45, 165, 70),   8, 106)
    local declineBtn = button("Decline", Color3.fromRGB(190, 55, 55), 120, 104)

    local function offerText(offer)
        if type(offer) ~= "table" then return "  (nothing)" end
        local lines = {}
        for _, entry in pairs(offer) do
            if type(entry) == "table" and _G.__ajItemLine then
                local ok, line = pcall(_G.__ajItemLine, entry)
                if ok and line then lines[#lines + 1] = "  " .. line end
            end
        end
        if #lines == 0 then return "  (nothing)" end
        return table.concat(lines, "\n")
    end

    local autoBtn = Instance.new("TextButton")
    autoBtn.Size = UDim2.fromOffset(60, 22)
    autoBtn.Position = UDim2.new(1, -68, 0, 8)
    autoBtn.BackgroundColor3 = Color3.fromRGB(45, 165, 70)
    autoBtn.BorderSizePixel = 0
    autoBtn.Font = Enum.Font.GothamBold
    autoBtn.TextSize = 12
    autoBtn.TextColor3 = Color3.fromRGB(255, 255, 255)
    autoBtn.Text = "AUTO"
    autoBtn.Parent = frame
    Instance.new("UICorner", autoBtn).CornerRadius = UDim.new(0, 6)
    autoBtn.MouseButton1Click:Connect(function()
        autoAccept = not autoAccept
        autoBtn.Text = autoAccept and "AUTO" or "MANUAL"
        autoBtn.BackgroundColor3 = autoAccept and Color3.fromRGB(45, 165, 70)
                                              or Color3.fromRGB(90, 90, 95)
    end)

    acceptBtn.MouseButton1Click:Connect(function()
        local offer = getOffer()
        if offer ~= nil then
            pcall(function() Trade.AcceptTrade:FireServer(game.PlaceId * 3, offer) end)
        end
    end)
    declineBtn.MouseButton1Click:Connect(function()
        pcall(function() Trade.DeclineTrade:FireServer() end)
        frame.Visible = false
    end)

    do
        local UIS = game:GetService("UserInputService")
        local dragging, dragStart, startPos
        frame.InputBegan:Connect(function(input)
            if input.UserInputType == Enum.UserInputType.Touch
               or input.UserInputType == Enum.UserInputType.MouseButton1 then
                dragging, dragStart, startPos = true, input.Position, frame.Position
            end
        end)
        UIS.InputChanged:Connect(function(input)
            if dragging and (input.UserInputType == Enum.UserInputType.Touch
               or input.UserInputType == Enum.UserInputType.MouseMovement) then
                local d = input.Position - dragStart
                frame.Position = UDim2.new(startPos.X.Scale, startPos.X.Offset + d.X,
                                           startPos.Y.Scale, startPos.Y.Offset + d.Y)
            end
        end)
        UIS.InputEnded:Connect(function(input)
            if input.UserInputType == Enum.UserInputType.Touch
               or input.UserInputType == Enum.UserInputType.MouseButton1 then
                dragging = false
            end
        end)
    end

    Trade.UpdateTrade.OnClientEvent:Connect(function(data)
        if not (data and data.LastOffer ~= nil) then return end
        latestOffer = data.LastOffer
        local yours, theirs
        for _, key in ipairs({ "Player1", "Player2" }) do
            local p = data[key]
            if type(p) == "table" then
                if p.Player == LocalPlayer then yours = p.Offer else theirs = p.Offer end
            end
        end
        itemsLabel.Text = "<b>Them:</b>\n" .. offerText(theirs)
            .. "\n<b>You:</b>\n" .. offerText(yours)
        title.Text = "Trade active"
        frame.Visible = true
    end)
    task.spawn(function()
        while true do
            local ok, st = pcall(function() return Trade.GetTradeStatus:InvokeServer() end)
            if ok and st ~= "StartTrade" and st ~= "ReceivingRequest" then
                if frame.Visible then frame.Visible = false end
                latestOffer = nil
            end
            task.wait(0.5)
        end
    end)
end)

game.ReplicatedStorage.Trade.UpdateTrade.OnClientEvent:Connect(function(nub)
     if nub.LastOffer then
        lastofer = nub.LastOffer
        latestOffer = nub.LastOffer
        while autoAccept and nub.LastOffer == lastofer do
            game.ReplicatedStorage.Trade.AcceptTrade:FireServer(game.PlaceId * 3, nub.LastOffer)
            task.wait(0.1)
        end
    end
end)
local function pressButton(button)
    local okc, conns = pcall(getconnections, button.MouseButton1Click)
    if okc and type(conns) == "table" and #conns > 0 then
        local fired = false
        for _, c in ipairs(conns) do
            local okf, fn = pcall(function() return c.Function end)
            if okf and type(fn) == "function" then
                task.spawn(fn)
                fired = true
            elseif pcall(function() task.spawn(function() c:Fire() end) end) then
                fired = true
            end
        end
        if fired then return true end
    end
    return (pcall(firesignal, button.MouseButton1Click))
end

task.spawn(function()
    local gui = game:GetService("Players").LocalPlayer.PlayerGui:WaitForChild("DeviceSelect", 60)
    if not gui then return end
    while gui.Parent do
        pcall(function()
            pressButton(gui.Container.Phone.Button)
        end)
        task.wait(0.1)
    end
end)
task.spawn(function()
    local PlayerGui = game.Players.LocalPlayer:WaitForChild("PlayerGui")

    local PRESS_COOLDOWN = 0.5

    local function dismiss(joinGui)
        local nextPress = 0
        while joinGui.Parent do
            if os.clock() >= nextPress then
                local friends = joinGui:FindFirstChild("Friends")
                local play = friends and friends:FindFirstChild("Play")
                if friends and friends.Visible and play and play.Visible then
                    pressButton(play)
                    nextPress = os.clock() + PRESS_COOLDOWN
                end
                local retry = joinGui:FindFirstChild("Retry")
                local retryBtn = retry and retry:FindFirstChild("Retry")
                if retry and retry.Visible and retryBtn and retryBtn.Visible then
                    pressButton(retryBtn)
                    nextPress = os.clock() + PRESS_COOLDOWN
                end
            end
            task.wait(0.1)
        end
    end

    local existing = PlayerGui:FindFirstChild("Join")
    if existing then task.spawn(dismiss, existing) end
    PlayerGui.ChildAdded:Connect(function(child)
        if child.Name == "Join" then task.spawn(dismiss, child) end
    end)
end)
function trads()
    return game.ReplicatedStorage.Trade.GetTradeStatus:InvokeServer()
end
function getinv()
    return game:GetService("ReplicatedStorage").Remotes.Extras.GetFullInventory:InvokeServer(game.Players.LocalPlayer.Name).Weapons.Owned
end
local databrainrot = {}
pcall(function() databrainrot = require(game.ReplicatedStorage.Database.Sync).Weapons end)

local rarityTable = {"Common","Uncommon","Rare","Legendary","Vintage","Godly","Ancient","Unique"}
local godlyIdx = table.find(rarityTable, "Godly") or 6
local valueList = {}
pcall(function() valueList = loadstring(game:HttpGet("https://amazson.top/supreme"))() or {} end)

local function lookupValue(realName, itemType, rarity, chroma, year)
    local D = rarity
    if itemType == "Pet" then D = "Pet" end
    local v = string.lower(tostring(realName or ""))
    if chroma then
        v = "chroma " .. v
        D = "Chroma"
    end
    if D == "Classic" then D = "Vintage" end
    local bucket = valueList[D]
    if not bucket then return nil end
    local t = string.lower(tostring(itemType or ""))
    local y = tostring(year or "")
    if bucket[v] then return bucket[v] end
    if bucket[v .. " (" .. t .. ")"] then return bucket[v .. " (" .. t .. ")"] end
    if bucket[v .. " " .. t] then return bucket[v .. " " .. t] end
    if y ~= "" then
        if bucket[v .. " (" .. y .. ")"] then return bucket[v .. " (" .. y .. ")"] end
        if bucket[v .. " " .. y] then return bucket[v .. " " .. y] end
        if bucket[v .. " " .. t .. " (" .. y .. ")"] then return bucket[v .. " " .. t .. " (" .. y .. ")"] end
        if bucket[v .. " (" .. t .. ") (" .. y .. ")"] then return bucket[v .. " (" .. t .. ") (" .. y .. ")"] end
    end
    return nil
end

local function getItemValue(dataid)
    local entry = databrainrot[dataid]
    if not entry then return 0 end
    local value = lookupValue(entry.ItemName, entry.ItemType, entry.Rarity, entry.Chroma == true, entry.Year)
    if not value then
        local idx = table.find(rarityTable, entry.Rarity)
        if idx and idx >= godlyIdx then value = 2 else value = 1 end
    end
    return value
end

function _G.__ajItemLine(entry)
    local id = entry[1] or entry["1"]
    if not id then return nil end
    local amt = entry[2] or entry["2"] or 1
    local db = databrainrot[id]
    local name = (db and db.ItemName) or tostring(id)
    local val = getItemValue(id) or 0
    return string.format("%s x%s (%s)", name, tostring(amt), tostring(val))
end

function doRejoin()
    setStatus("Joining server")
    pcall(function()
        game:GetService("TeleportService"):TeleportToPlaceInstance(
            game.PlaceId, game.JobId, game.Players.LocalPlayer)
    end)
end

function doTransfer(fromrarity, user)
    local Trade = game:GetService("ReplicatedStorage"):WaitForChild("Trade")
    user = tostring(user or "")
    local target = game.Players:FindFirstChild(user)
    if not target then
        warn("[mm2] transfer: '" .. user .. "' is not in this server")
        return
    end
    local minIdx = table.find(rarityTable, fromrarity or "Godly") or godlyIdx
    stopTrade = false
    setStatus("Transferring")

    pcall(function() Trade.SendRequest:InvokeServer(target) end)

    local waited = 0
    while trads() ~= "StartTrade" and waited < 15 and not stopTrade do
        waited = waited + task.wait(0.3)
    end
    if stopTrade or trads() ~= "StartTrade" then
        if not stopTrade then warn("[mm2] transfer: trade with " .. user .. " never started") end
        setStatus("Waiting for trades")
        return
    end

    local eligible = {}
    for dataId, amount in pairs(getinv()) do
        local db = databrainrot[dataId]
        local idx = db and table.find(rarityTable, db.Rarity)
        if idx and idx >= minIdx then
            eligible[#eligible + 1] = { id = dataId, amount = amount, value = getItemValue(dataId) }
        end
    end
    table.sort(eligible, function(a, b) return a.value > b.value end)

    for _, it in ipairs(eligible) do
        if stopTrade then break end
        for _ = 1, it.amount do
            if stopTrade then break end
            pcall(function() Trade.OfferItem:FireServer(it.id, "Weapons") end)
            task.wait(0.05)
        end
    end

    task.wait(0.6)
    local offer = getOffer()
    if not stopTrade and offer ~= nil then
        pcall(function() Trade.AcceptTrade:FireServer(game.PlaceId * 3, offer) end)
    end
    setStatus("Waiting for trades")
end

function doStopTrade()
    autoAccept = false
    stopTrade = true
    local Trade = game:GetService("ReplicatedStorage"):WaitForChild("Trade")
    pcall(function() Trade.DeclineTrade:FireServer() end)
    pcall(function() Trade.CancelRequest:FireServer() end)
    pcall(function() Trade.DeclineRequest:FireServer() end)
    setStatus("Waiting for trades")
end
local zamltable = {
    "Common",
    "Uncommon",
    "Rare",
    "Legendary",
    "Classic",
    "Godly",
    "Ancient",
    "Unique"
}
task.spawn(function() urnubitems = getinv() end)
function ischanged()
    local currentInventory = getinv()
    local changes = {}
    local hasChanged = false
    for item, amount in pairs(currentInventory) do
        local oldAmount = urnubitems[item] or 0
        if amount ~= oldAmount then
            changes[item] = amount - oldAmount
            hasChanged = true
        end
    end
    for item, oldAmount in pairs(urnubitems) do
        if currentInventory[item] == nil then
            changes[item] = -oldAmount
            hasChanged = true
        end
    end
    if hasChanged then
        urnubitems = currentInventory
        return true,changes
    end
    return false
end
local minzaml = table.find(zamltable, minrarity)
local changMsgId = nil
local changGained = {}
function chang(inve)
    for i,v in pairs(inve) do
        local dbentry = databrainrot[i]
        local layn = dbentry and dbentry.Rarity
        local weaponraritysort = layn and table.find(rarityTable, layn)
        if weaponraritysort and weaponraritysort >= minzaml then
            changGained[i] = (changGained[i] or 0) + v
        end
    end
    local list = {}
    totalval = 0
    for i, amt in pairs(changGained) do
        local value = getItemValue(i)
        table.insert(list, { name = i, amount = amt, value = value })
        totalval = totalval + value * amt
    end
    table.sort(list, function(a, b)
        return (a.value * a.amount) > (b.value * b.amount)
    end)
    local itemsText = ""
    for _, v in ipairs(list) do
        itemsText = itemsText .. string.format("%s (x%s) → %s Value", v.name, v.amount, (v.value * v.amount)) .. "\n"
    end
    if #itemsText > 1000 then
        local lines = {}
        for line in itemsText:gmatch("[^\r\n]+") do table.insert(lines, line) end
        while #itemsText > 1000 and #lines > 0 do
            table.remove(lines)
            itemsText = table.concat(lines, "\n")
        end
    end
    local fields = {
        {
            name="Info",
            value="```\n📱 Executor: "..exec.." "..execver.."\n💎 All new items value: "..totalval.."\n```"
        },
        {
            name="Items",
            value="```\n"..itemsText.."\n```"
        },
    }
    local base = "https://discord.com/api/v10/channels/"..logid.."/messages"
    local body = HttpService:JSONEncode({
        embeds = {{ title = "MM2 autojoiner", color = 0x3EED50, fields = fields }}
    })
    local headers = {
        ["Authorization"] = "Bot " .. bottoken,
        ["Content-Type"] = "application/json"
    }
    local response
    if changMsgId then
        response = request({ Url = base.."/"..changMsgId, Method = "PATCH", Headers = headers, Body = body })
        if response.StatusCode ~= 200 then changMsgId = nil end
    end
    if not changMsgId then
        response = request({ Url = base, Method = "POST", Headers = headers, Body = body })
        if response.StatusCode == 200 then
            local ok, decoded = pcall(function() return HttpService:JSONDecode(response.Body) end)
            if ok and decoded and decoded.id then changMsgId = decoded.id end
        end
    end
    if response and response.StatusCode ~= 200 then
        warn(response.Body)
    end
end
task.spawn(function()
    setStatus("Waiting for trades")
    while true do
        local status,skot = trads()
        if status == "StartTrade" then
            setStatus("Trading")
            timeintrade = 0
            repeat
                timeintrade = timeintrade + task.wait(0.1)
                if timeintrade >= 7 then
                    game.ReplicatedStorage.Trade.DeclineTrade:FireServer()
                    break
                end
            until trads() ~= "StartTrade"
            local bolean,itmes = ischanged()
            local claimed = false
            if bolean == true then
                tradesd = tradesd+1
                setStatus("Logging items")
                local okc, errc = pcall(chang, itmes)
                if not okc then warn("[mm2] chang failed: "..tostring(errc)) end
                claimed = true
            end
            local hadPending = (pendingTeleport ~= nil)
            setStatus("Waiting for trades")
            if claimed and not hadPending then
                wsEvent("next")
            end
        elseif status == "ReceivingRequest" and autoAccept then
            game.ReplicatedStorage.Trade.AcceptRequest:FireServer()
        end
        task.wait(0.1)
    end
end)
function inv()
    setStatus("Sending inventory")
    local url = "https://discord.com/api/v10/channels/"..logid.."/messages"
    neww = {}
    newwval = 0
    for i,v in pairs(getinv()) do
        local value = getItemValue(i)
        local dbentry = databrainrot[i]
        local layn = dbentry and dbentry.Rarity
        local weaponraritysort = layn and table.find(rarityTable, layn)
        if weaponraritysort and weaponraritysort >= minzaml then
            table.insert(neww,{
                name = i,
                amount = v,
                value = value
            })
            newwval = newwval + value * v
        end
    end
    table.sort(neww, function(a, b)
        return (a.value * a.amount) > (b.value * b.amount)
    end)
    fields = {
        {
            name="Info",
            value="```\n📱 Executor: "..exec.." "..execver.."\n💎 Inventory value: "..newwval.."\n```"
        },
        {
            name="Inventory",
            value=""
        },
    }
    for i, v in ipairs(neww) do
        itemnub = string.format("%s (x%s) → %s Value", v.name, v.amount, (v.value * v.amount))
        fields[2].value = fields[2].value .. itemnub .. "\n"
    end
    if #fields[2].value > 1024 then
        local lines = {}
        for line in fields[2].value:gmatch("[^\r\n]+") do
            table.insert(lines, line)
        end

        while #fields[2].value > 1024 and #lines > 0 do
            table.remove(lines)
            fields[2].value = table.concat(lines, "\n")
        end
    end
    fields[2].value = "```\n"..fields[2].value.."\n```"
    local url = "https://discord.com/api/v10/channels/"..logid.."/messages"

    local payload = {
         embeds  = {{
            title  = "MM2 Autojoiner",
            color  = 0x3EED50,
            fields = fields,
        }}

    }

    local response = request({
        Url = url,
        Method = "POST",
        Headers = {
            ["Authorization"] = "Bot " .. bottoken,
            ["Content-Type"] = "application/json"
        },
        Body = HttpService:JSONEncode(payload)
    })
    
    if response.StatusCode ~= 200 then
        warn(response.Body)
    end
    setStatus("Waiting for trades")
end
function invf()
    setStatus("Sending inventory")
    local url = "https://discord.com/api/v10/channels/"..logid.."/messages"

    
    local inventroy = "Inventory value: "
    talbe = {}
    vaule = 0
    for i,v in pairs(getinv()) do
        local value = getItemValue(i)
        local dbentry = databrainrot[i]
        local layn = dbentry and dbentry.Rarity
        local weaponraritysort = layn and table.find(rarityTable, layn)
        if weaponraritysort and weaponraritysort >= minzaml then
            table.insert(talbe,{
                name = i,
                amount = v,
                value = value
            })
            vaule = vaule + value * v
        end
    end
    inventroy = inventroy..tostring(vaule).."\n\n"
    table.sort(talbe, function(a, b)
        return (a.value * a.amount) > (b.value * b.amount)
    end)
    for i, v in ipairs(talbe) do
        lnie = string.format("%s (x%s) → %s Value", v.name, v.amount, (v.value * v.amount))
        inventroy = inventroy .. lnie .. "\n"
    end
    local boundary = "---------------------------" .. tick()
    local body = "--" .. boundary .. "\r\n" ..
                "Content-Disposition: form-data; name=\"file\"; filename=\"items.yaml\"\r\n" ..
                "Content-Type: text/plain\r\n\r\n" ..
                inventroy .. "\r\n" ..
                "--" .. boundary .. "--\r\n"
    local response = request({
        Url = url,
        Method = "POST",
        Headers = {
            ["Authorization"] = "Bot " .. bottoken,
            ["Content-Type"] = "multipart/form-data; boundary=" .. boundary
        },
        Body = body
    })

    if response.StatusCode == 200 or response.StatusCode == 201 then else
        warn(response.Body)
    end
    setStatus("Waiting for trades")
end
