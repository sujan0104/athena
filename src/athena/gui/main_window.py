from PySide6.QtWidgets import (
    QHBoxLayout,
    QMainWindow,
    QStackedWidget,
    QVBoxLayout,
    QWidget,
)

from athena.gui.components.sidebar import Sidebar
from athena.gui.pages.home import HomePage
from athena.gui.themes.style import APP_STYLE


class MainWindow(QMainWindow):
    """Main Athena Desktop window."""

    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Athena Desktop")
        self.resize(1500, 900)

        self._build_ui()

        self.setStyleSheet(APP_STYLE)

    def _build_ui(self) -> None:
        root = QWidget()
        self.setCentralWidget(root)

        layout = QHBoxLayout(root)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        self.sidebar = Sidebar()

        self.stack = QStackedWidget()

        self.home_page = HomePage()

        self.stack.addWidget(self.home_page)

        layout.addWidget(self.sidebar)
        layout.addWidget(self.stack)

        self.sidebar.page_changed.connect(self.change_page)

    def change_page(self, index: int) -> None:
        if index == 0:
            self.stack.setCurrentWidget(self.home_page)

        # Future pages
        # elif index == 1:
        #     self.stack.setCurrentWidget(self.chat_page)