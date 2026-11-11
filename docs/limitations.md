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

Disabling local automation does not revoke broker-side API
permissions. External trading access requires separate
credential and permission controls.
This repository is not evidence of broker-side revocation.

No live credentials, account identifiers, order journals,
private trading records, or executable production order
submission code should be published.

## Performance Claims

No claim is made of stable profitability, superior
investment returns, or a fully verified automated
trading lifecycle.