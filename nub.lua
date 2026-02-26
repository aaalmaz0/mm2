--[[
	ElvebreddParser.lua
	Roblox Luau Module — Elvebredd Adopt Me Value Calculator Parser
	Source: https://elvebredd.com/adopt-me-calculator

	USAGE EXAMPLE:
		local ElvebreddParser = require(game.ServerScriptService.ElvebreddParser)

		-- Fetch all pet values from Elvebredd
		local values = ElvebreddParser.FetchValues()

		-- Look up a single pet
		local shadowDragon = ElvebreddParser.GetPet(values, "Shadow Dragon")
		print(shadowDragon.value, shadowDragon.neon_value, shadowDragon.mega_value)

		-- Evaluate a trade
		local myOffer    = { { name = "Shadow Dragon",    variant = "Regular" } }
		local theirOffer = { { name = "Frost Dragon",     variant = "Neon"    },
		                     { name = "Parrot",           variant = "Regular" } }
		local result = ElvebreddParser.EvaluateTrade(values, myOffer, theirOffer)
		print(result.verdict)      -- "WIN", "FAIR", or "LOSE"
		print(result.myTotal)
		print(result.theirTotal)
		print(result.difference)
]]

-- ┌─────────────────────────────────────────────────────────┐
-- │                      DEPENDENCIES                        │
-- └─────────────────────────────────────────────────────────┘
local HttpService = game:GetService("HttpService")

-- ┌─────────────────────────────────────────────────────────┐
-- │                      CONSTANTS                           │
-- └─────────────────────────────────────────────────────────┘

-- The public Elvebredd API endpoint that powers the calculator page.
-- If Elvebredd ever changes their API path, update this constant.
local BASE_URL       = "https://elvebredd.com"
local ITEMS_ENDPOINT = BASE_URL .. "/api/items"    -- returns JSON array of all items
local CALC_ENDPOINT  = BASE_URL .. "/adopt-me-calculator" -- fallback page fetch

-- Multipliers applied on top of the base (regular) value
local VARIANT_MULTIPLIER = {
	Regular = 1.0,
	Neon    = 4.0,   -- 4× regular (approximate Elvebredd standard)
	Mega    = 16.0,  -- 4 Neons = 16× regular
}

-- Enhancement add-ons (applied after variant multiplier)
local ENHANCEMENT_BONUS = {
	None  = 0.0,
	Fly   = 0.10,  -- +10% on top of variant value
	Ride  = 0.07,  -- +7%
	FR    = 0.18,  -- Fly + Ride combined
}

-- Win/Fair/Lose thresholds (fraction of the larger side)
-- If your side is ≥ 90% of theirs → WIN (you got overpay)
-- If the ratio is between 85%–110% → FAIR
-- Otherwise → LOSE
local FAIR_THRESHOLD_LOW  = 0.85
local FAIR_THRESHOLD_HIGH = 1.15

-- ┌─────────────────────────────────────────────────────────┐
-- │                    MODULE TABLE                          │
-- └─────────────────────────────────────────────────────────┘
local ElvebreddParser = {}
ElvebreddParser.__index = ElvebreddParser

-- ┌─────────────────────────────────────────────────────────┐
-- │                  PRIVATE HELPERS                         │
-- └─────────────────────────────────────────────────────────┘

--- Attempt to GET a URL and return the decoded JSON body.
--- Returns (data, nil) on success, or (nil, errorMsg) on failure.
local function safeFetch(url: string): (any?, string?)
	local ok, response = pcall(function()
		return HttpService:GetAsync(url, true)
	end)
	if not ok then
		return nil, "HttpService:GetAsync failed — " .. tostring(response)
	end

	local decoded, decodeErr = pcall(function()
		return HttpService:JSONDecode(response)
	end)
	if not decoded then
		return nil, "JSONDecode failed — " .. tostring(decodeErr)
	end

	return decodeErr, nil   -- pcall stores result in second var when ok=true
end

--- Normalise a pet name for case-insensitive lookup.
local function normalise(name: string): string
	return name:lower():gsub("%s+", " "):match("^%s*(.-)%s*$")
end

--- Build a lookup dictionary keyed by normalised pet name.
local function buildIndex(items: {any}): {[string]: any}
	local index = {}
	for _, item in ipairs(items) do
		if item.name then
			index[normalise(item.name)] = item
		end
	end
	return index
end

--- Resolve the effective numeric value for a pet entry given variant + enhancement.
local function resolveValue(petEntry: any, variant: string?, enhancement: string?): number
	variant     = variant     or "Regular"
	enhancement = enhancement or "None"

	-- Prefer explicit neon_value / mega_value fields when available
	local base: number
	if variant == "Mega" and petEntry.mega_value then
		base = tonumber(petEntry.mega_value) or 0
	elseif variant == "Neon" and petEntry.neon_value then
		base = tonumber(petEntry.neon_value) or 0
	else
		base = tonumber(petEntry.value) or 0
	end

	-- Apply variant multiplier if no explicit field was found
	if not petEntry.neon_value and variant ~= "Regular" then
		local mult = VARIANT_MULTIPLIER[variant] or 1.0
		base = base * mult
	end

	-- Apply enhancement bonus
	local bonus = ENHANCEMENT_BONUS[enhancement] or 0.0
	base = base + (base * bonus)

	return base
end

-- ┌─────────────────────────────────────────────────────────┐
-- │                  PUBLIC API                              │
-- └─────────────────────────────────────────────────────────┘

--[[
	ElvebreddParser.FetchValues()
	
	Fetches the full item/pet value list from the Elvebredd API.
	
	Returns a ValueStore table:
	{
	    raw   : table   -- the raw JSON array returned by the API
	    index : table   -- dictionary keyed by normalised pet name
	    ok    : bool    -- false if the fetch failed
	    err   : string? -- error message when ok == false
	}
--]]
function ElvebreddParser.FetchValues()
	local store = {
		raw   = {},
		index = {},
		ok    = false,
		err   = nil,
	}

	local data, err = safeFetch(ITEMS_ENDPOINT)
	if err then
		-- Elvebredd may serve the item data embedded in the calculator page.
		-- As a graceful degradation we return an empty but valid store so the
		-- rest of the API still functions (useful in Studio offline tests).
		store.err = "Could not fetch Elvebredd values: " .. err
		warn("[ElvebreddParser] " .. store.err)
		return store
	end

	-- The API can return either a plain array or a wrapper like { items = {...} }
	local items
	if typeof(data) == "table" then
		if data.items and typeof(data.items) == "table" then
			items = data.items
		elseif data[1] ~= nil then
			items = data          -- plain array
		else
			-- Try common wrapper keys
			for _, key in ipairs({ "data", "pets", "values", "results" }) do
				if data[key] and typeof(data[key]) == "table" then
					items = data[key]
					break
				end
			end
		end
	end

	if not items then
		store.err = "Unexpected API response shape — could not locate items array."
		warn("[ElvebreddParser] " .. store.err)
		return store
	end

	store.raw   = items
	store.index = buildIndex(items)
	store.ok    = true
	return store
end

--[[
	ElvebreddParser.GetPet(store, petName)
	
	Look up a single pet by name (case-insensitive).
	Returns the raw pet entry table, or nil if not found.
	
	Fields typically present in the returned table:
	    .id          : number
	    .name        : string
	    .value       : number   (regular)
	    .neon_value  : number?
	    .mega_value  : number?
	    .rarity      : string   ("Common"|"Uncommon"|"Rare"|"Ultra-Rare"|"Legendary")
	    .category    : string   ("Pet"|"Vehicle"|"Toy"|"Potion"|...)
	    .demand      : string?
--]]
function ElvebreddParser.GetPet(store, petName: string): any?
	assert(typeof(petName) == "string", "petName must be a string")
	return store.index[normalise(petName)]
end

--[[
	ElvebreddParser.GetValue(store, petName, variant?, enhancement?)
	
	Returns the resolved numeric value for a pet.
	    variant     : "Regular" | "Neon" | "Mega"     (default "Regular")
	    enhancement : "None"    | "Fly"  | "Ride" | "FR"  (default "None")
	
	Returns 0 if the pet is not found.
--]]
function ElvebreddParser.GetValue(
	store,
	petName:     string,
	variant:     string?,
	enhancement: string?
): number
	local entry = ElvebreddParser.GetPet(store, petName)
	if not entry then
		warn("[ElvebreddParser] Pet not found: " .. tostring(petName))
		return 0
	end
	return resolveValue(entry, variant, enhancement)
end

--[[
	ElvebreddParser.EvaluateTrade(store, myOffer, theirOffer)
	
	Evaluates a two-sided trade and returns a result table.
	
	Each offer is an array of item descriptors:
	{
	    name        : string,
	    variant     : "Regular"|"Neon"|"Mega"?    (default "Regular")
	    enhancement : "None"|"Fly"|"Ride"|"FR"?   (default "None")
	}
	
	Returns:
	{
	    verdict    : "WIN" | "FAIR" | "LOSE"
	    myTotal    : number   -- total value of your offer
	    theirTotal : number   -- total value of their offer
	    difference : number   -- theirTotal - myTotal  (positive = you gain)
	    ratio      : number   -- myTotal / theirTotal  (1.0 = perfectly equal)
	    breakdown  : table    -- per-item value details for both sides
	}
--]]
function ElvebreddParser.EvaluateTrade(store, myOffer: {any}, theirOffer: {any})
	assert(typeof(myOffer)    == "table", "myOffer must be a table")
	assert(typeof(theirOffer) == "table", "theirOffer must be a table")

	local function sumOffer(offer)
		local total     = 0
		local breakdown = {}
		for _, item in ipairs(offer) do
			local v = ElvebreddParser.GetValue(
				store,
				item.name or "",
				item.variant,
				item.enhancement
			)
			total += v
			table.insert(breakdown, {
				name        = item.name,
				variant     = item.variant     or "Regular",
				enhancement = item.enhancement or "None",
				resolvedValue = v,
			})
		end
		return total, breakdown
	end

	local myTotal,    myBreakdown    = sumOffer(myOffer)
	local theirTotal, theirBreakdown = sumOffer(theirOffer)

	local ratio: number
	if theirTotal == 0 then
		ratio = math.huge
	else
		ratio = myTotal / theirTotal
	end

	-- WFL verdict: comparing what YOU get vs. what YOU give
	-- ratio > 1.15  → you're giving more than you get            → LOSE
	-- ratio < 0.85  → you're giving less than you get            → WIN (overpay for you)
	-- 0.85–1.15     → balanced                                   → FAIR
	local verdict: string
	if ratio < FAIR_THRESHOLD_LOW then
		verdict = "WIN"    -- you receive more value than you give
	elseif ratio > FAIR_THRESHOLD_HIGH then
		verdict = "LOSE"   -- you give more value than you receive
	else
		verdict = "FAIR"
	end

	return {
		verdict      = verdict,
		myTotal      = myTotal,
		theirTotal   = theirTotal,
		difference   = theirTotal - myTotal,
		ratio        = ratio,
		breakdown    = {
			myOffer    = myBreakdown,
			theirOffer = theirBreakdown,
		},
	}
end

--[[
	ElvebreddParser.Search(store, query, maxResults?)
	
	Fuzzy-ish search across all pet names.
	Returns up to maxResults (default 10) matching entries.
	Matches are sorted by how early in the name the query appears.
--]]
function ElvebreddParser.Search(store, query: string, maxResults: number?): {any}
	maxResults = maxResults or 10
	local q       = normalise(query)
	local results = {}

	for name, entry in pairs(store.index) do
		local pos = name:find(q, 1, true)
		if pos then
			table.insert(results, { entry = entry, pos = pos })
		end
	end

	table.sort(results, function(a, b)
		if a.pos ~= b.pos then return a.pos < b.pos end
		return (a.entry.name or "") < (b.entry.name or "")
	end)

	local out = {}
	for i = 1, math.min(#results, maxResults) do
		table.insert(out, results[i].entry)
	end
	return out
end

--[[
	ElvebreddParser.FilterByRarity(store, rarity)
	
	Returns all pets that match the given rarity string.
	Rarity options (case-insensitive):
	    "Common" | "Uncommon" | "Rare" | "Ultra-Rare" | "Legendary"
--]]
function ElvebreddParser.FilterByRarity(store, rarity: string): {any}
	local r   = rarity:lower()
	local out = {}
	for _, entry in ipairs(store.raw) do
		if entry.rarity and entry.rarity:lower() == r then
			table.insert(out, entry)
		end
	end
	return out
end

--[[
	ElvebreddParser.TopN(store, n?, descending?)
	
	Returns the top N pets sorted by their regular value.
	descending defaults to true (highest first).
--]]
function ElvebreddParser.TopN(store, n: number?, descending: boolean?): {any}
	n          = n          or 10
	descending = (descending == nil) and true or descending

	local copy = {}
	for _, entry in ipairs(store.raw) do
		if entry.value then
			table.insert(copy, entry)
		end
	end

	table.sort(copy, function(a, b)
		local va = tonumber(a.value) or 0
		local vb = tonumber(b.value) or 0
		return descending and (va > vb) or (va < vb)
	end)

	local out = {}
	for i = 1, math.min(#copy, n) do
		table.insert(out, copy[i])
	end
	return out
end

--[[
	ElvebreddParser.PrintTradeResult(result)
	
	Pretty-prints the result table from EvaluateTrade() to the Output console.
	Handy for debugging in Studio.
--]]
function ElvebreddParser.PrintTradeResult(result)
	local SEPARATOR = string.rep("─", 48)
	print(SEPARATOR)
	print(string.format("  VERDICT  : %s", result.verdict))
	print(string.format("  MY TOTAL : %.4f", result.myTotal))
	print(string.format("  THEIR    : %.4f", result.theirTotal))
	print(string.format("  DIFF     : %+.4f (positive = I gain)", result.difference))
	print(string.format("  RATIO    : %.4f  (1.0 = equal)", result.ratio))
	print(SEPARATOR)

	print("  [MY OFFER]")
	for _, item in ipairs(result.breakdown.myOffer) do
		print(string.format("    %-30s %-8s %-4s => %.4f",
			item.name, item.variant, item.enhancement, item.resolvedValue))
	end

	print("  [THEIR OFFER]")
	for _, item in ipairs(result.breakdown.theirOffer) do
		print(string.format("    %-30s %-8s %-4s => %.4f",
			item.name, item.variant, item.enhancement, item.resolvedValue))
	end
	print(SEPARATOR)
end

-- ┌─────────────────────────────────────────────────────────┐
-- │              OFFLINE / MOCK DATA LOADER                  │
-- │  Use this when HttpService is unavailable (Studio tests) │
-- └─────────────────────────────────────────────────────────┘

--[[
	ElvebreddParser.LoadMockData(petTable)
	
	Manually load a table of pet entries so the parser can be used
	without a live HTTP call (useful for offline Studio testing or
	when you cache values locally).
	
	petTable should be an array of tables like:
	{
	    { name="Shadow Dragon", value=100, neon_value=500, mega_value=2200, rarity="Legendary" },
	    { name="Frost Dragon",  value=60,  neon_value=280, mega_value=1200, rarity="Legendary" },
	    ...
	}
	
	Returns a ValueStore in the same format as FetchValues().
--]]
function ElvebreddParser.LoadMockData(petTable: {any})
	assert(typeof(petTable) == "table", "petTable must be a table")
	return {
		raw   = petTable,
		index = buildIndex(petTable),
		ok    = true,
		err   = nil,
	}
end

-- ┌─────────────────────────────────────────────────────────┐
-- │               BUILT-IN MOCK DATASET                      │
-- │  A small snapshot of well-known Adopt Me pet values so   │
-- │  the module works immediately without an API call.        │
-- └─────────────────────────────────────────────────────────┘
local BUILTIN_MOCK_PETS = {
	-- LEGENDARY
	{ name="Shadow Dragon",      value=120,  neon_value=540,  mega_value=2300, rarity="Legendary"  },
	{ name="Frost Dragon",       value=70,   neon_value=320,  mega_value=1400, rarity="Legendary"  },
	{ name="Bat Dragon",         value=65,   neon_value=290,  mega_value=1300, rarity="Legendary"  },
	{ name="Giraffe",            value=55,   neon_value=250,  mega_value=1100, rarity="Legendary"  },
	{ name="Owl",                value=40,   neon_value=185,  mega_value=800,  rarity="Legendary"  },
	{ name="Parrot",             value=38,   neon_value=175,  mega_value=760,  rarity="Legendary"  },
	{ name="Kitsune",            value=30,   neon_value=140,  mega_value=600,  rarity="Legendary"  },
	{ name="Unicorn",            value=18,   neon_value=80,   mega_value=360,  rarity="Legendary"  },
	{ name="Dragon",             value=16,   neon_value=72,   mega_value=320,  rarity="Legendary"  },
	{ name="Golden Dragon",      value=14,   neon_value=62,   mega_value=280,  rarity="Legendary"  },
	{ name="Diamond Dragon",     value=20,   neon_value=92,   mega_value=400,  rarity="Legendary"  },
	{ name="Goldhorn",           value=25,   neon_value=115,  mega_value=500,  rarity="Legendary"  },
	{ name="Frost Fury",         value=22,   neon_value=100,  mega_value=440,  rarity="Legendary"  },
	{ name="Arctic Reindeer",    value=28,   neon_value=130,  mega_value=560,  rarity="Legendary"  },
	{ name="Crow",               value=10,   neon_value=45,   mega_value=200,  rarity="Legendary"  },
	{ name="Dodo",               value=9,    neon_value=40,   mega_value=180,  rarity="Legendary"  },
	{ name="Phoenix",            value=18,   neon_value=82,   mega_value=360,  rarity="Legendary"  },
	{ name="Cerberus",           value=15,   neon_value=68,   mega_value=300,  rarity="Legendary"  },
	{ name="Evil Unicorn",       value=12,   neon_value=54,   mega_value=240,  rarity="Legendary"  },
	-- ULTRA-RARE
	{ name="Albino Monkey",      value=8,    neon_value=36,   mega_value=160,  rarity="Ultra-Rare" },
	{ name="King Bee",           value=7,    neon_value=32,   mega_value=144,  rarity="Ultra-Rare" },
	{ name="Shiba Inu",          value=5,    neon_value=22,   mega_value=100,  rarity="Ultra-Rare" },
	{ name="Red Panda",          value=4,    neon_value=18,   mega_value=80,   rarity="Ultra-Rare" },
	{ name="Wolpertinger",       value=4,    neon_value=18,   mega_value=80,   rarity="Ultra-Rare" },
	{ name="Koala",              value=3,    neon_value=14,   mega_value=60,   rarity="Ultra-Rare" },
	{ name="Sloth",              value=3,    neon_value=14,   mega_value=60,   rarity="Ultra-Rare" },
	{ name="Snow Puma",          value=3,    neon_value=13,   mega_value=56,   rarity="Ultra-Rare" },
	-- RARE
	{ name="Turtle",             value=6,    neon_value=27,   mega_value=120,  rarity="Rare"       },
	{ name="Kangaroo",           value=5,    neon_value=22,   mega_value=98,   rarity="Rare"       },
	{ name="Capybara",           value=2.5,  neon_value=11,   mega_value=48,   rarity="Rare"       },
	{ name="Fennec Fox",         value=2,    neon_value=9,    mega_value=40,   rarity="Rare"       },
	{ name="Dalmation",          value=1.5,  neon_value=7,    mega_value=30,   rarity="Rare"       },
	-- UNCOMMON
	{ name="Bunny",              value=0.5,  neon_value=2,    mega_value=9,    rarity="Uncommon"   },
	{ name="Lamb",               value=0.5,  neon_value=2,    mega_value=9,    rarity="Uncommon"   },
	-- COMMON
	{ name="Dog",                value=0.1,  neon_value=0.45, mega_value=2,    rarity="Common"     },
	{ name="Cat",                value=0.1,  neon_value=0.45, mega_value=2,    rarity="Common"     },
	-- POTIONS / ITEMS
	{ name="Ride Potion",        value=2,    rarity="Potion",   category="Potion"  },
	{ name="Fly Potion",         value=3,    rarity="Potion",   category="Potion"  },
	{ name="Unicorn Stroller",   value=4,    rarity="Legendary",category="Vehicle" },
}

--[[
	ElvebreddParser.GetBuiltinStore()
	
	Returns a ValueStore pre-loaded with the built-in mock pet dataset.
	Use this when you don't want to make an HTTP call at all.
--]]
function ElvebreddParser.GetBuiltinStore()
	return ElvebreddParser.LoadMockData(BUILTIN_MOCK_PETS)
end

-- ┌─────────────────────────────────────────────────────────┐
-- │                     MODULE RETURN                        │
-- └─────────────────────────────────────────────────────────┘
return ElvebreddParser
