import sys

from PySide6.QtWidgets import QApplication

from app_ui import LaptopAI


def main():
    app = QApplication(sys.argv)

    window = LaptopAI()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()