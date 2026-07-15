# Contrarian Greed MCP

Version-controlled source for the Contrarian Greed production engine.

## Goal

Move all deterministic market-data collection, scoring, freshness checks, contribution reconciliation, and paper-strategy state into MCP. Google Sheets remains a presentation and audit sink. ChatGPT reads the current skill and independently audits the MCP output before writing AI Model, Web, and Combined opinions.

## Migration status

- Existing production: `contrarian-mcp.vercel.app`
- Current model: `v0.9.1-RSI-ICI132`
- Migration target: MCP-owned calculations with skill-based audit/opinion layer
- Production is not modified until preview tests and parity checks pass.
