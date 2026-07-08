from __future__ import annotations

import logging

from athena.core.service import BaseService


class LoggerService(BaseService):
    """Provides application-wide logging."""

    def __init__(self) -> None:
        self._logger = logging.getLogger("athena")

    @property
    def name(self) -> str:
        return "LoggerService"

    def start(self) -> None:
        logging.basicConfig(
            level=logging.INFO,
            format="[%(levelname)s] %(message)s",
        )
        self._logger.info("Logger service started.")

    def stop(self) -> None:
        self._logger.info("Logger service stopped.")

    def get_logger(self) -> logging.Logger:
        return self._logger
