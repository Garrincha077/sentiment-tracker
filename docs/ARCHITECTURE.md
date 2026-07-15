# Contrarian Greed MCP v1 architecture

## Responsibilities

### MCP — deterministic source of truth

MCP owns:

- raw source collection and immutable observation metadata;
- all numerical transforms and scores;
- final weights and thresholds;
- contribution ledger and reconciliation;
- Coverage, Freshness, Agreement, Source Quality and Confidence;
- paper-strategy state and execution ledger;
- explicit fresh, stale, provisional and unavailable states.

### Skill — audit and opinion overlay

The current Google Doc skill remains mandatory. ChatGPT must:

1. read the current skill revision;
2. verify `/health`, `/status`, `/snapshot` and `/model-config`;
3. require matching model version and build SHA;
4. independently reconcile contributions to Composite;
5. verify GuruFocus weekly-cache policy and ICI history disclosure;
6. perform current web research without changing numerical Composite;
7. produce AI Model Opinion, AI Web Opinion and AI Combined Opinion;
8. write the audited result to Google Sheets.

### Google Sheets — presentation and audit sink

Sheets must not calculate production RSI, DXY, VIX term structure or Composite. It may retain display formulas, charts and read-back validation formulas.

## Data collectors

- SPY daily adjusted/unadjusted close history and Wilder RSI(14)
- Cboe Equity Put/Call and Total Put/Call session history
- VIX close and VIX futures M1/M2 term structure
- NAAIM and AAII weekly observations
- ICI verified official observations with calendar gaps
- market breadth, HY OAS and HYG/IEF
- GuruFocus weekly cached insider ratio and boundary score
- six-pair Synthetic DXY full history, EMA10/EMA20 and 30W slope
- CFTC Legacy COT and zero-weight TFF diagnostics
- CNN Fear & Greed

## Required API contract

`/snapshot` must expose, for every input:

- raw value and unit;
- observation date, release date, fetched_at and fresh_until;
- source URL and source quality;
- scoring method and transform parameters;
- score, effective weight and contribution;
- fresh/stale/provisional/unavailable status;
- reason for every non-fresh state.

It must also expose Core, DXY, COT, RSI, Composite, coverage, freshness, agreement, source quality, confidence, action state, paper state and reconciliation delta.

## Migration gates

Production is not changed until all gates pass:

1. version/config/build parity;
2. 250+ SPY closes and RSI parity within 0.01;
3. Cboe raw-value parity for the last 10 completed sessions;
4. DXY EMA and slope calculated from the exact stored six-pair series;
5. VIX M1/M2 values independently visible in snapshot;
6. Breadth/Credit leaves independently visible;
7. contribution sum equals Composite within 0.01;
8. current production and preview results compared over at least five completed sessions;
9. no silent renormalization;
10. rollback deployment identified before promotion.
