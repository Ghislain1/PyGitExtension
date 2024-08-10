
# Built-in imports
import sys

# Externe Imports
from PyQt6.QtWidgets import QApplication
from qt_material import apply_stylesheet
# Legacy imports
from  ui.main_window import MainWindow



def main ():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    
    # Apply theme
    apply_stylesheet(app,"dark_cyan.xml")
    sys.exit(app.exec())

if __name__ == "__main__":
    main()