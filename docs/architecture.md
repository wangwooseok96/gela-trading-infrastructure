# System Architecture

Historical research workflow:

Market Data
    |
    v
Daily Signal Generation
    |
    v
Trade Intent Generation
    |
    v
Shadow-State Order Planning
    |
    v
Execution Journal / State Management
    |
    v
Brokerage Reconciliation
    |
    v
Operational Monitoring

The original system also contained a live order submission
path. It is not included in this offline showcase.

Function-level evidence includes:
- build_production_signal_snapshot
- generate_next_open_intents
- prepare_shadow_orders
- reconcile_live_submission_with_broker
- verify_live_broker_shadow_positions
- recover_execution_cycle_registry_from_disk_atomic

Function presence alone does not establish successful
end-to-end operation or runtime reliability.