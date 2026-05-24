# Data Context

## Committed Inputs

- Folder: `fins2026/week5/data`
- Files: 3

### `fins2026/week5/data/README.md`
- Size: 361 B
- Type: `.md`

### `fins2026/week5/data/yahoo_crypto_20_since_2019.txt`
- Size: 220 B
- Type: `.txt`
- Format: plain-text one-item-per-line list
- Entries: 20
- Preview: `BTC-USD`, `ETH-USD`, `XRP-USD`, `ADA-USD`, `LTC-USD`, ... and 15 more

### `fins2026/week5/data/yahoo_crypto_intro_5.txt`
- Size: 80 B
- Type: `.txt`
- Format: plain-text one-item-per-line list
- Entries: 5
- Preview: `BTC-USD`, `ETH-USD`, `XRP-USD`, `ADA-USD`, `DOGE-USD`

## Generated Data

- Folder: `fins2026/week5/results/data`
- Status: generated locally and not committed by default


## Timing And Alignment Notes

- Stage 3: generate out-of-sample portfolio weights, daily portfolio returns, FT-style OOS portfolio figures, and point-in-time factsheet figures from the cleaned Stage 2 panel using only past data at each rebalance date.
- the same folder now contains both a research pack and a point-in-time factsheet pack.
- keep Stage 3 daily portfolio returns indexed by the earned `return_date` rather than a synthetic month-end label.
- the factsheet layer should translate the same Stage 3 engine into app-style point-in-time views of holdings, concentration, turnover, and BTC/ETH exposure.
