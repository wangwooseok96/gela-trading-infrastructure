# Algorithmic Trading Infrastructure

GELA x TradeUP 2026 Global AI Trading Challenge

## Overview

Python-based equity trading research and brokerage-integration
project developed between September and November 2026.

Environment:
- Python
- Pandas
- Jupyter Notebook
- TradeUP OpenAPI
- Windows 11

The research covered approximately 20 US equities.

## Engineering Scope

The original private project contains components for:

- Market data processing and daily signal generation
- Trade intent generation and order planning
- Shadow-state and execution journal management
- Brokerage order and position reconciliation
- Execution safeguards and recovery logic
- Read-only operational monitoring

## Current Status

The competition has concluded.

Automated trading has been permanently disabled.
All future trading decisions and executions are manual.

Historical production trading code is not distributed here.

## Important Limitations

The original system had an unresolved exit-signal indexing defect.
A scheduled TSLA exit was not generated as intended.

The project does not demonstrate a fully validated
automated buy/sell lifecycle or consistent profitability.

See docs/limitations.md for details.

## Repository Status

Offline technical showcase with three synthetic Python modules and 27 passing unit tests.

Any future demonstration code must be independently reviewed,
sanitized, and restricted to offline or simulated operation.

## Offline Demonstration Modules

- Position reconciliation: synthetic broker and shadow-state comparison.
- Order lifecycle: in-memory transitions, fill events, and idempotency.
- T+6 exit indexing: synthetic rolling-window defect illustration.

## Running Tests

Run from the repository root:

    python -B -m unittest discover -s tests -p "test_*.py" -v

The 27 tests cover only independently written offline demonstrations.
They do not validate the historical production trading system.

## Historical Limitations

The original trading system had an unresolved SELL exit-indexing defect.
Automated trading remains disabled; future trades are manual.
No reliable profitability or fully validated execution is claimed.

See docs/limitations.md and docs/exit_index_case_study.md.
