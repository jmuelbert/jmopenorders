# -*- coding: utf-8 -*-
# Copyright (c) 2019-2020 Jürgen Mülbert. All rights reserved.
#
# Licensed under the EUPL, Version 1.2 or – as soon they
# will be approved by the European Commission - subsequent
# versions of the EUPL (the "Licence");
# You may not use this work except in compliance with the
# Licence.
# You may obtain a copy of the Licence at:
#
# https://joinup.ec.europa.eu/page/eupl-text-11-12
#
# Unless required by applicable law or agreed to in
# writing, software distributed under the Licence is
# distributed on an "AS IS" basis,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
# express or implied.
# See the Licence for the specific language governing
# permissions and limitations under the Licence.
#
# Lizenziert unter der EUPL, Version 1.2 oder - sobald
# diese von der Europäischen Kommission genehmigt wurden -
# Folgeversionen der EUPL ("Lizenz");
# Sie dürfen dieses Werk ausschließlich gemäß
# dieser Lizenz nutzen.
# Eine Kopie der Lizenz finden Sie hier:
#
# https://joinup.ec.europa.eu/page/eupl-text-11-12
#
# Sofern nicht durch anwendbare Rechtsvorschriften
# gefordert oder in schriftlicher Form vereinbart, wird
# die unter der Lizenz verbreitete Software "so wie sie
# ist", OHNE JEGLICHE GEWÄHRLEISTUNG ODER BEDINGUNGEN -
# ausdrücklich oder stillschweigend - verbreitet.
# Die sprachspezifischen Genehmigungen und Beschränkungen
# unter der Lizenz sind dem Lizenztext zu entnehmen.
"""Global application logging.

All modules use the same global logging object. No messages will be emitted
until the logger is started.
"""
from logging import Formatter
from logging import Logger as _Logger
from logging import NullHandler
from logging import StreamHandler
from typing import Any

__all__ = ["logger", "Logger"]


class Logger(_Logger):
    """Message logger."""

    LOGFMT = "%(asctime)s;%(levelname)s;%(name)s;%(message)s"

    def __init__(self, name: str = "") -> None:
        """Initialize this logger.

        Loggers with the same name refer to the same underlying object.
        Names are hierarchical, e.g. 'parent.child' defines a logger that is a
        descendant of 'parent'.

        Args:
            name: logger name (application name by default)
        """
        # With a NullHandler, client code may make logging calls without regard
        # to whether the logger has been started yet. The standard Logger API
        # may be used to add and remove additional handlers, but the
        # NullHandler should always be left in place.
        super().__init__(name or __name__.split(".")[0])
        self.addHandler(NullHandler())  # default to no output
        return

    def start(self, level: str = "WARN", stream: Any = None) -> None:
        """Start logging to a stream.

        Until the logger is started, no messages will be emitted. This applies
        to all loggers with the same name and any child loggers.

        Multiple streams can be logged to by calling start() for each one.
        Calling start() more than once for the same stream will result in
        duplicate records to that stream.

        Messages less than the given priority level will be ignored. The
        default level conforms to the *nix* convention that a successful run
        should produce no diagnostic output. Call setLevel() to change the
        logger's priority level after it has been stared. Available levels and
        their suggested meanings:

            DEBUG - output useful for developers
            INFO - trace normal program flow, especially external interactions
            WARN - an abnormal condition was detected that might need attention
            ERROR - an error was detected but execution continued
            CRITICAL - an error was detected and execution was halted

        Args:
            level: logger priority level
            stream: output stream (stderr by default)
        """
        handler = StreamHandler(stream)
        handler.setFormatter(Formatter(self.LOGFMT))
        self.addHandler(handler)
        self.setLevel(level.upper())
        return

    def stop(self) -> None:
        """Stop logging with this logger."""
        for handler in self.handlers[1:]:
            # Remove everything but the NullHandler.
            self.removeHandler(handler)
        return


logger = Logger()
