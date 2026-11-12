from __future__ import annotations

import signal
from typing import Callable


class GracefulShutdown:
    def __init__(self):
        self._handlers: list[Callable[[], None]] = []

    def register(self, handler: Callable[[], None]) -> None:
        self._handlers.append(handler)

    def handle(self, signum, frame) -> None:
        for handler in self._handlers:
            handler()


def register_shutdown_handler(handler: Callable[[], None]) -> GracefulShutdown:
    shutdown = GracefulShutdown()
    shutdown.register(handler)
    signal.signal(signal.SIGINT, shutdown.handle)
    signal.signal(signal.SIGTERM, shutdown.handle)
    return shutdown
