# Known Limitations and Safety Boundaries

## Historical Exit-Signal Failure

A rolling-window indexing discrepancy affected
time-based exit evaluation.

The TSLA T+6 exit expected on November 3, 2026
did not generate the required SELL intent.

This defect remains unresolved in the historical
production system.

## Operational Safety

Automated trading has been disabled.

The historical broker API credentials retained trading
permissions at the time of the safety audit.
Therefore, this repository must never be treated
as evidence that all external trading access was revoked.

No live credentials, account identifiers, order journals,
private trading records, or executable production order
submission code should be published.

## Performance Claims

No claim is made of stable profitability, superior
investment returns, or a fully verified automated
trading lifecycle.