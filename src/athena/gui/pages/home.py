from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import QLabel, QVBoxLayout, QWidget


class HomePage(QWidget):
    """Athena home dashboard."""

    def __init__(self) -> None:
        super().__init__()

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.setSpacing(20)

        title = QLabel("Welcome to Athena")

        font = QFont()
        font.setPointSize(28)
        font.setBold(True)

        title.setFont(font)
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)

        subtitle = QLabel("Your AI Operating System")

        subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(title)
        layout.addWidget(subtitle)