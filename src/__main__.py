
# Built-in imports
import sys

# Externe Imports
from PyQt6.QtWidgets import QApplication
from qt_material import apply_stylesheet

# Legacy imports
from core import info
from  ui.main_window import MainWindow
from core.logger import log



def main ():

    log.info("##############################  Appis Loading  ---")             
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    
    # Apply theme
    apply_stylesheet(app, info.APP_STYLE_SHEET)
    log.debug(f" ############################## App uses Style: {info.APP_STYLE_SHEET} ---")   
    sys.exit(app.exec())

  

if __name__ == "__main__":
    main()