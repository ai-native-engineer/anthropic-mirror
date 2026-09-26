<!-- source: https://claude.com/marketplace/connectors/coinversa-pulse -->

Connector URL`https://mcp.coinversa.ai/mcp`

More[Documentation (opens in new tab)](https://docs.coinversa.ai/mcp/setup)[Support (opens in new tab)](mailto:chat@coinversaa.ai)[Privacy policy (opens in new tab)](https://coinversa.ai/privacy)

Coinversa Pulse gives Claude read-only access to the full Hyperliquid data universe: every tracked wallet classified into behavioral cohorts, indexed trade history with PnL attribution, reconstructed position lifecycles (entry, exit, hold time, MAE/MFE), live positions and open interest, liquidation heatmaps, builder-dex revenue analytics, and HIP-4 outcome contracts.

Ask questions the way a desk analyst would and get chain-derived answers:

- Who are the best traders on Hyperliquid this month, deduped by owner rather than wallet?

- Is BTC crowded right now? Where are the liquidation clusters? Did open interest build into this move?

- Are smart-money cohorts long or short ETH, and were they rotating before the move?

- Profile a wallet: win rate, average hold, drawdown curve, biggest wins and losses.

- Which builder frontends earn the most fees, and is their user base smart money or exit liquidity?

- Which HIP-4 outcome markets are most active, who trades them, and are those traders hedged with perps?

Coverage spans native Hyperliquid perps plus seven builder dexes (xyz, flx, vntl, hyna, km, abcd, cash), so commodities (xyz:GOLD, km:OIL), equities (cash:TSLA) and crypto perps are all queryable, with a canonical cross-market asset registry that resolves synonyms such as PAXG to GOLD. Call pulse\_global\_stats at any time for exact current coverage: wallets, trades, volume and data window.

Over 100 tools, all read-only. Coinversa Pulse never places orders, never touches funds, and never asks for wallet keys. It is analytics only, and nothing it returns is investment advice.

Requires a Coinversa account. Connect with your Coinversa login or an API key from coinversa.ai/developers; the plan on your account determines which tools and rate limits are available.

## Tools

* builder\_cohorts
* builder\_fills
* builder\_journey
* builder\_leaderboard
* builder\_lifecycle
* builder\_orders
* builder\_overlap
* builder\_profile
* builder\_retention
* builder\_traders
* hip4\_cross\_product\_overlap
* hip4\_daily\_volume
* hip4\_most\_active
* hip4\_outcome
* hip4\_outcome\_recent\_trades
* hip4\_outcome\_summary
* hip4\_outcomes
* hip4\_perp\_position\_context
* hip4\_questions
* hip4\_recent\_settlements
* hip4\_top\_traders
* hip4\_trader\_outcomes
* list\_asset
* list\_assets

Show all 101 tools

Only use connectors from developers you trust. Anthropic does not control which tools developers make available and cannot verify that they will work as intended or that they won’t change.

## Related connectors

![](https://assets.claude.com/a8994e05e594a562449127d44e0fe86c31d8e41c.svg?w=128&fit=max&auto=format)

### [Google Drive](https://claude.com/marketplace/connectors/google-drive)

Search, read, and upload files instantly

[Add Google Drive in Claude (opens in new tab)](https://claude.ai/directory/b89f7865-a755-4f86-8062-c3bd651740ce "Add in Claude")

![](https://assets.claude.com/89209c1f16bf517eb431ff08e811de0778d70689.svg?w=128&fit=max&auto=format)

### [Supabase](https://claude.com/marketplace/connectors/supabase)

Manage databases, authentication, and storage

[Add Supabase in Claude (opens in new tab)](https://claude.ai/directory/11ca66fc-1e98-49d5-ab9b-7cb4672a8f10 "Add in Claude")

![](https://www.google.com/s2/favicons?domain=monday.com&sz=96)

### [monday.com](https://claude.com/marketplace/connectors/monday)

monday.com project management & CRM for projects, tasks, portfolios, boards, workflows, milestones, dependencies, forms, dashboards, cross-project portfolio status, and critical paths.

[Add monday.com in Claude (opens in new tab)](https://claude.ai/directory/49e0f9ba-7d45-4fb6-b098-55eec956fbc6 "Add in Claude")

![](https://assets.claude.com/73fb34c4126e99aa21f0f63e48c061963454ee06.svg?w=128&fit=max&auto=format)

### [Addepar MCP](https://claude.com/marketplace/connectors/addepar)

Bring Addepar portfolio intelligence into Claude

[Add Addepar MCP in Claude (opens in new tab)](https://claude.ai/directory/bc2b011f-5db9-4aef-9df0-fe500264075d "Add in Claude")

![](https://assets.claude.com/11f81df36177359e07a76903f59116d6f7e4f856.jpg?w=128&fit=max&auto=format)

### [Box](https://claude.com/marketplace/connectors/box)

Search, edit and get insights on your Box content

[Add Box in Claude (opens in new tab)](https://claude.ai/directory/a5380429-c773-4180-b642-301418240c8c "Add in Claude")

![](https://assets.claude.com/e64f9962a277a8943b084a17b6a9386a7eb95a61.svg?w=128&fit=max&auto=format)

### [Miro](https://claude.com/marketplace/connectors/miro)

Access and create new content on Miro boards

[Add Miro in Claude (opens in new tab)](https://claude.ai/directory/72480fb8-32ed-4075-b1c4-79e09c858b29 "Add in Claude")
