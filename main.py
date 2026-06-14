"""
Rasengan Desktop App — main entry point.
Launches the PyQt6 window and bootstraps all modules.
"""
import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import Qt
from modules.ui import MainWindow


def main():
    # High-DPI support
    app = QApplication(sys.argv)
    app.setApplicationName("Rasengan")
    app.setOrganizationName("Naruto")

    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()