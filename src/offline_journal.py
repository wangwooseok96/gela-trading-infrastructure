"""Synthetic, in-memory order lifecycle demonstration.

Not copied from the historical trading system.
No broker API, networking, files, or order execution.
"""

from dataclasses import dataclass
from decimal import Decimal, InvalidOperation


class JournalError(ValueError):
    pass


def positive_quantity(value):
    if isinstance(value, bool):
        raise JournalError("Invalid quantity")
    try:
        q = Decimal(str(value))
    except (InvalidOperation, TypeError, ValueError):
        raise JournalError("Invalid quantity")
    if not q.is_finite() or q <= 0:
        raise JournalError("Quantity must be positive and finite")
    return q


@dataclass
class Order:
    symbol: str
    quantity: Decimal
    state: str = "PLANNED"
    filled: Decimal = Decimal("0")


class OfflineJournal:
    def __init__(self):
        self.orders = {}
        self.fill_events = {}

    def plan(self, order_id, symbol, quantity):
        if not isinstance(order_id, str) or not order_id:
            raise JournalError("Invalid order ID")
        if not isinstance(symbol, str) or not symbol:
            raise JournalError("Invalid symbol")

        q = positive_quantity(quantity)

        if order_id in self.orders:
            old = self.orders[order_id]
            if old.symbol != symbol or old.quantity != q:
                raise JournalError("Conflicting order ID")
            return old

        order = Order(symbol, q)
        self.orders[order_id] = order
        return order

    def submit(self, order_id):
        order = self.orders[order_id]
        if order.state == "SUBMITTED":
            return order
        if order.state != "PLANNED":
            raise JournalError("Invalid submission transition")
        order.state = "SUBMITTED"
        return order

    def record_fill(self, order_id, event_id, quantity):
        order = self.orders[order_id]
        q = positive_quantity(quantity)

        if not isinstance(event_id, str) or not event_id:
            raise JournalError("Invalid fill event ID")

        previous = self.fill_events.get(event_id)
        if previous is not None:
            if previous != (order_id, q):
                raise JournalError("Conflicting fill event")
            return order

        if order.state not in ("SUBMITTED", "PARTIAL"):
            raise JournalError("Fill not permitted in current state")

        if order.filled + q > order.quantity:
            raise JournalError("Fill exceeds planned quantity")

        order.filled += q
        order.state = (
            "FILLED" if order.filled == order.quantity
            else "PARTIAL"
        )
        self.fill_events[event_id] = (order_id, q)
        return order

    def cancel(self, order_id):
        order = self.orders[order_id]
        if order.state == "CANCELLED":
            return order
        if order.state not in ("PLANNED", "SUBMITTED", "PARTIAL"):
            raise JournalError("Cancellation not permitted")
        order.state = "CANCELLED"
        return order