"""Unit tests for the isolated synthetic journal."""

import sys
import unittest
from pathlib import Path

sys.path.insert(
    0, str(Path(__file__).resolve().parents[1] / "src")
)

from offline_journal import OfflineJournal, JournalError


class JournalTests(unittest.TestCase):

    def setUp(self):
        self.j = OfflineJournal()
        self.j.plan("ORDER_1", "DEMO_A", "5")

    def test_initial_state(self):
        self.assertEqual(self.j.orders["ORDER_1"].state, "PLANNED")

    def test_idempotent_plan(self):
        a = self.j.orders["ORDER_1"]
        b = self.j.plan("ORDER_1", "DEMO_A", "5.0")
        self.assertIs(a, b)

    def test_conflicting_order_id_rejected(self):
        with self.assertRaises(JournalError):
            self.j.plan("ORDER_1", "DEMO_A", "6")

    def test_submission(self):
        self.j.submit("ORDER_1")
        self.assertEqual(
            self.j.orders["ORDER_1"].state, "SUBMITTED"
        )

    def test_duplicate_submission(self):
        self.j.submit("ORDER_1")
        self.j.submit("ORDER_1")
        self.assertEqual(len(self.j.orders), 1)

    def test_partial_then_full_fill(self):
        self.j.submit("ORDER_1")
        self.j.record_fill("ORDER_1", "FILL_A", "2")
        self.assertEqual(self.j.orders["ORDER_1"].state, "PARTIAL")
        self.j.record_fill("ORDER_1", "FILL_B", "3")
        self.assertEqual(self.j.orders["ORDER_1"].state, "FILLED")

    def test_duplicate_fill_event(self):
        self.j.submit("ORDER_1")
        self.j.record_fill("ORDER_1", "FILL_A", "2")
        self.j.record_fill("ORDER_1", "FILL_A", "2")
        self.assertEqual(
            self.j.orders["ORDER_1"].filled, 2
        )

    def test_conflicting_fill_event(self):
        self.j.submit("ORDER_1")
        self.j.record_fill("ORDER_1", "FILL_A", "2")
        with self.assertRaises(JournalError):
            self.j.record_fill("ORDER_1", "FILL_A", "3")

    def test_overfill_rejected(self):
        self.j.submit("ORDER_1")
        with self.assertRaises(JournalError):
            self.j.record_fill("ORDER_1", "FILL_A", "6")
        self.assertEqual(self.j.orders["ORDER_1"].filled, 0)

    def test_fill_before_submit_rejected(self):
        with self.assertRaises(JournalError):
            self.j.record_fill("ORDER_1", "FILL_A", "1")

    def test_cancelled_order_cannot_fill(self):
        self.j.cancel("ORDER_1")
        with self.assertRaises(JournalError):
            self.j.record_fill("ORDER_1", "FILL_A", "1")

    def test_filled_order_cannot_resubmit(self):
        self.j.submit("ORDER_1")
        self.j.record_fill("ORDER_1", "FILL_A", "5")
        with self.assertRaises(JournalError):
            self.j.submit("ORDER_1")

    def test_negative_quantity_rejected(self):
        with self.assertRaises(JournalError):
            self.j.plan("ORDER_2", "DEMO_B", "-1")


if __name__ == "__main__":
    unittest.main()