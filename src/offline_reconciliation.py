"""Offline position reconciliation demonstration.

Synthetic inputs only. No broker connectivity or order execution.
This is an illustrative implementation, not original production code.
"""

from decimal import Decimal, InvalidOperation


def quantity(value):
    """Convert a nonnegative finite share quantity to Decimal."""
    if isinstance(value, bool):
        raise ValueError("Boolean quantity is invalid")

    try:
        result = Decimal(str(value))
    except (InvalidOperation, ValueError, TypeError):
        raise ValueError("Invalid share quantity")

    if not result.is_finite() or result < 0:
        raise ValueError("Quantity must be finite and nonnegative")

    return result


def reconcile_positions(shadow_positions, broker_positions):
    """Compare shadow holdings with synthetic broker holdings.

    broker_positions:
        {symbol: {"quantity": value, "salable_qty": value}}

    The quantity field represents total holdings.
    salable_qty is deliberately excluded from position equality.
    """
    if not isinstance(shadow_positions, dict):
        raise TypeError("Shadow positions must be a dictionary")

    if not isinstance(broker_positions, dict):
        raise TypeError("Broker positions must be a dictionary")

    discrepancies = []

    for symbol in sorted(set(shadow_positions) | set(broker_positions)):
        if not isinstance(symbol, str) or not symbol:
            raise ValueError("Invalid symbol")

        shadow_qty = quantity(shadow_positions.get(symbol, 0))

        broker_record = broker_positions.get(symbol)

        if broker_record is None:
            broker_qty = Decimal(0)
        else:
            if not isinstance(broker_record, dict):
                raise TypeError("Invalid broker record")
            if "quantity" not in broker_record:
                raise ValueError("Missing broker total quantity")

            broker_qty = quantity(broker_record["quantity"])

        if shadow_qty != broker_qty:
            discrepancies.append({
                "symbol": symbol,
                "shadow_quantity": str(shadow_qty),
                "broker_quantity": str(broker_qty),
            })

    return discrepancies