from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QMainWindow


class MainWindow(QMainWindow):
    """Main application window for Athena Desktop."""

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Athena Desktop")
        self.resize(1000, 650)

        status = QLabel("🟢 Initializing...")
        status.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setCentralWidget(status)
