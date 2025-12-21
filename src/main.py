# Built-in imports
import sys
from PyQt6.QtWidgets import QApplication

# Externe Imports
from app.application import Application


# sys.path.append(".")


def main():
    # Create the Qt Application: Setup
    qt_app = QApplication(sys.argv)
    app = Application(qt_app)
    app.run()
    sys.exit(qt_app.exec())


if __name__ == "__main__":
    main()
