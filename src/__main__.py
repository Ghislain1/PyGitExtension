# Built-in imports
import sys

# Externe Imports
from ui.app import App
from qt_material import apply_stylesheet


sys.path.append(".")


def main():
    app = App(sys.argv)

    app.showMainWindow()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
