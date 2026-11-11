# GELA x TradeUP 2026 | Algorithmic Trading Infrastructure

**Offline engineering showcase | Python | Reconciliation | State Management | Testing**

An engineering portfolio project derived from research conducted
during the GELA x TradeUP 2026 Global AI Trading Challenge
(September-November 2026).

The historical project explored equity trading signals, order
planning, brokerage integration, state reconciliation, and
operational safety controls.

**This repository contains independently written, offline
demonstrations only. It does not contain the historical
production trading system or executable brokerage integrations.**

## Engineering Highlights

### 1. Position Reconciliation
`src/offline_reconciliation.py`

- Compares synthetic broker holdings with shadow-state positions.
- Uses exact decimal arithmetic for share quantities.
- Separates total holdings from salable quantities.
- Detects missing positions and quantity discrepancies.
- Rejects invalid quantity inputs.

### 2. Order Lifecycle and Idempotency
`src/offline_journal.py`

- Models planned, submitted, partially filled, filled,
  and cancelled order states in memory.
- Demonstrates idempotent planning and fill-event handling.
- Rejects conflicting event identifiers and overfills.
- Validates state transitions without submitting orders.

### 3. Rolling-Window Exit Indexing
`src/exit_index_demo.py`

- Illustrates a stale fixed-index failure mode.
- Evaluates synthetic T+6 exits using ordered sessions.
- Covers shifting windows and boundary conditions.
- Fails closed when required session history is missing.

This is a synthetic illustration, not a production defect fix.

## Repository Structure

| Path | Purpose |
| --- | --- |
| `src/offline_reconciliation.py` | Synthetic position comparison |
| `src/offline_journal.py` | In-memory order lifecycle |
| `src/exit_index_demo.py` | T+6 indexing illustration |
| `tests/` | 27 offline unit tests |
| `docs/architecture.md` | Historical workflow overview |
| `docs/exit_index_case_study.md` | Indexing case study |
| `docs/limitations.md` | Safety and validation boundaries |

## Running Tests

Requirements: Python 3 and its standard library.

From the repository root:

```powershell
python -B -m unittest discover -s tests -p "test_*.py" -v
```

The 27 tests validate the three standalone demonstration
modules. They do not validate the historical brokerage
integration, live execution, or end-to-end trading lifecycle.

No brokerage credentials or network connection are required
to run these demonstrations.

## Historical System and Safety Boundaries

The historical system included research components for market
data processing, signal generation, order planning, execution
journaling, broker reconciliation, and monitoring.

The presence of those components does not establish that the
historical system was fully validated or reliable in production.

A historical TSLA T+6 SELL intent expected on November 3, 2026
was not generated as intended. The original indexing issue
remains unresolved.

Automated trading execution was disabled on November 5, 2026.
All subsequent trading decisions and executions are manual.

This repository makes no claim of:
- Verified production trading safety
- Fully functioning automated buy/sell execution
- Historical defect remediation in the original system
- Consistent profitability or superior investment returns

## Technical Documentation

- [Architecture](docs/architecture.md)
- [Rolling-Window Exit Case Study](docs/exit_index_case_study.md)
- [Known Limitations](docs/limitations.md)

## Scope

This project is an offline technical showcase of selected
software-engineering and operational-control concepts.

It is not a trading service, investment recommendation,
or deployable live trading application.
