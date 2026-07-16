from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QPushButton, QVBoxLayout, QWidget


class Sidebar(QWidget):
    """Athena navigation sidebar."""

    page_changed = Signal(int)

    def __init__(self) -> None:
        super().__init__()

        self.setFixedWidth(240)

        self.buttons: list[QPushButton] = []

        layout = QVBoxLayout(self)
        layout.setContentsMargins(15, 25, 15, 25)
        layout.setSpacing(10)

        pages = [
            "🏠  Home",
            "💬  Chat",
            "⚡  Skills",
            "🤖  AI",
            "🧠  Memory",
            "🔄  Automation",
            "🐧  Linux",
            "📦  Plugins",
            "⚙  Settings",
        ]

        for index, text in enumerate(pages):
            button = QPushButton(text)
            button.setCursor(Qt.CursorShape.PointingHandCursor)
            button.clicked.connect(
                lambda checked=False, i=index: self.change_page(i)
            )

            self.buttons.append(button)
            layout.addWidget(button)

        layout.addStretch()

        self.change_page(0)

    def change_page(self, index: int) -> None:
        for button in self.buttons:
            button.setProperty("active", False)
            button.style().unpolish(button)
            button.style().polish(button)

        self.buttons[index].setProperty("active", True)
        self.buttons[index].style().unpolish(self.buttons[index])
        self.buttons[index].style().polish(self.buttons[index])

        self.page_changed.emit(index)