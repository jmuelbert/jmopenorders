from logging import Logger as _Logger
from typing import Any

class Logger(_Logger):
    LOGFMT: str = ...
    def __init__(self, name: str = ...) -> None: ...
    def start(self, level: str = ..., stream: Any = ...) -> None: ...
    def stop(self) -> None: ...

logger: Any
