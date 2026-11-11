"""Synthetic rolling-window indexing demonstration.

This is NOT the historical production implementation.
No market data, broker API, or trading capabilities.
"""


def illustrative_fixed_index_check(
    entry_index, signal_index, holding_sessions=6
):
    """Illustrate a potentially stale window-index comparison."""
    return signal_index - entry_index >= holding_sessions


def exit_due_by_session_sequence(
    sessions, entry_session, holding_sessions=6
):
    """Evaluate a holding period using ordered session identities.

    The latest entry in sessions is the current evaluation session.
    Session identities must be strictly increasing integers.
    """
    if (
        isinstance(holding_sessions, bool)
        or not isinstance(holding_sessions, int)
        or holding_sessions < 1
    ):
        raise ValueError("Invalid holding period")

    if not isinstance(sessions, (list, tuple)) or not sessions:
        raise ValueError("Invalid session sequence")

    if any(
        isinstance(s, bool) or not isinstance(s, int)
        for s in sessions
    ):
        raise ValueError("Session identities must be integers")

    if any(
        a >= b for a, b in zip(sessions, sessions[1:])
    ):
        raise ValueError("Sessions must be strictly increasing")

    if entry_session not in sessions:
        raise ValueError("Entry session unavailable: fail closed")

    entry_position = sessions.index(entry_session)
    current_position = len(sessions) - 1

    return (
        current_position - entry_position >= holding_sessions
    )