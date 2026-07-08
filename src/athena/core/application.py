from __future__ import annotations

from typing import List

from PySide6.QtWidgets import QApplication

from athena.core.logger import LoggerService
from athena.core.service import BaseService
from athena.gui.main_window import MainWindow


class AthenaApplication:
    """Main application controller."""

    def __init__(self) -> None:
        self.qt_app = QApplication([])

        self.services: List[BaseService] = [
            LoggerService(),
        ]

        self.window = MainWindow()

    def start(self) -> None:
        """Start all services."""
        for service in self.services:
            service.start()

    def stop(self) -> None:
        """Stop all services."""
        for service in reversed(self.services):
            service.stop()

    def run(self) -> int:
        """Run Athena."""
        self.start()

        self.window.show()

        exit_code = self.qt_app.exec()

        self.stop()

        return exit_code
