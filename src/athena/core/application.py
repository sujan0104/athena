from PySide6.QtWidgets import QApplication

from athena.gui.main_window import MainWindow


class AthenaApplication:
    """Main application controller."""

    def __init__(self):
        self.app = QApplication([])
        self.window = MainWindow()

    def run(self):
        self.window.show()
        self.app.exec()
