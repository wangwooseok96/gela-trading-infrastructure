"""Tests using synthetic quantities and fictional symbols."""

import sys
import unittest
from pathlib import Path

sys.path.insert(
    0,
    str(Path(__file__).resolve().parents[1] / "src")
)

from offline_reconciliation import reconcile_positions


class ReconciliationTests(unittest.TestCase):

    def test_matching_positions(self):
        shadow = {"DEMO_A": "5", "DEMO_B": "2"}
        broker = {
            "DEMO_A": {"quantity": "5", "salable_qty": "5"},
            "DEMO_B": {"quantity": "2", "salable_qty": "2"},
        }
        self.assertEqual(reconcile_positions(shadow, broker), [])

    def test_quantity_mismatch_detected(self):
        shadow = {"DEMO_A": "5"}
        broker = {"DEMO_A": {"quantity": "3"}}
        issues = reconcile_positions(shadow, broker)
        self.assertEqual(len(issues), 1)
        self.assertEqual(issues[0]["symbol"], "DEMO_A")

    def test_salable_quantity_is_not_total_holdings(self):
        shadow = {"DEMO_A": "5"}
        broker = {
            "DEMO_A": {
                "quantity": "5",
                "salable_qty": "0.5",
            }
        }
        self.assertEqual(reconcile_positions(shadow, broker), [])

    def test_missing_broker_position_detected(self):
        shadow = {"DEMO_A": "5"}
        self.assertEqual(
            len(reconcile_positions(shadow, {})),
            1
        )

    def test_invalid_negative_position_rejected(self):
        with self.assertRaises(ValueError):
            reconcile_positions(
                {"DEMO_A": "-1"},
                {"DEMO_A": {"quantity": "0"}}
            )

    def test_fractional_shares(self):
        shadow = {"DEMO_A": "0.5"}
        broker = {
            "DEMO_A": {
                "quantity": "0.50",
                "salable_qty": "0.25",
            }
        }
        self.assertEqual(reconcile_positions(shadow, broker), [])


if __name__ == "__main__":
    unittest.main()