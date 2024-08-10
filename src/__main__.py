
# Built-in imports
import sys

# Externe Imports
from PyQt6.QtWidgets import QApplication

# Legacy imports
from  ui.main_window import MainWindow



def main ():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()