from __future__ import annotations

from typing import Any, Callable


class WebSocketManager:
    def __init__(self):
        self.subscribers: list[Callable[[str], None]] = []

    def subscribe(self, callback: Callable[[str], None]) -> None:
        self.subscribers.append(callback)

    def publish(self, message: str) -> None:
        for callback in self.subscribers:
            callback(message)
