"""Context window firewall to block role-swap tokens across a sliding window."""

from collections import deque
from typing import Iterable, Deque


class ContextFirewall:
    """Stateful detector for role-swap attempts within recent chat history.

    The firewall keeps the last ``window_size`` messages and scans them for
    role-swap markers such as ``"### Assistant:"``.  When ``process`` is called
    with a new message, it updates the window and returns ``True`` if no markers
    are present; otherwise ``False``.
    """

    DEFAULT_MARKERS = (
        "### Assistant:",
        "###assistant:",
        "### System:",
        "### system:",
        "### User:",
        "### user:",
    )

    def __init__(self, window_size: int = 4, markers: Iterable[str] | None = None) -> None:
        self.window_size = window_size
        self.markers = tuple(m.lower() for m in (markers or self.DEFAULT_MARKERS))
        self._window: Deque[str] = deque(maxlen=window_size)

    def reset(self) -> None:
        """Clear the stored message history."""

        self._window.clear()

    def process(self, message: str) -> bool:
        """Add ``message`` to history and return ``True`` if allowed.

        Parameters
        ----------
        message:
            The next chat message in sequence.

        Returns
        -------
        bool
            ``True`` if the message passes the firewall, ``False`` if a
            role-swap token is detected in the sliding window.
        """

        self._window.append(message)
        combined = " ".join(self._window).lower()
        return not any(token in combined for token in self.markers)
