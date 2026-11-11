"""Offline tests for a synthetic T+6 indexing case."""

import sys
import unittest
from pathlib import Path

sys.path.insert(
    0, str(Path(__file__).resolve().parents[1] / "src")
)

from exit_index_demo import (
    illustrative_fixed_index_check,
    exit_due_by_session_sequence,
)


class ExitIndexTests(unittest.TestCase):

    def test_before_six_sessions(self):
        for n in range(6):
            sessions = list(range(100, 101 + n))
            self.assertFalse(
                exit_due_by_session_sequence(sessions, 100)
            )

    def test_exactly_six_sessions(self):
        self.assertTrue(
            exit_due_by_session_sequence(
                list(range(100, 107)), 100
            )
        )

    def test_after_six_sessions(self):
        self.assertTrue(
            exit_due_by_session_sequence(
                list(range(100, 109)), 100
            )
        )

    def test_fixed_index_example_misses_due_exit(self):
        # Illustrative 1200-bar window index, not production code.
        self.assertFalse(
            illustrative_fixed_index_check(1199, 1199)
        )

    def test_rolling_window_still_detects_due_exit(self):
        # Synthetic 1200-session window advances six sessions.
        entry = 2199
        window = list(range(1006, 2206))
        self.assertEqual(len(window), 1200)
        self.assertTrue(
            exit_due_by_session_sequence(window, entry)
        )

    def test_missing_entry_fails_closed(self):
        with self.assertRaises(ValueError):
            exit_due_by_session_sequence(
                list(range(200, 210)), 100
            )

    def test_unsorted_sessions_rejected(self):
        with self.assertRaises(ValueError):
            exit_due_by_session_sequence(
                [100, 102, 101], 100
            )

    def test_invalid_holding_period_rejected(self):
        with self.assertRaises(ValueError):
            exit_due_by_session_sequence(
                [100, 101], 100, holding_sessions=0
            )


if __name__ == "__main__":
    unittest.main()