from __future__ import annotations

from typing import Any, Dict, Optional


class SpeechRecognizer:
    def __init__(self, enabled: bool = False):
        self.enabled = enabled

    def recognize(self, transcript: str | None = None) -> str | None:
        if not self.enabled:
            return transcript
        return transcript or "walk forward"
