# Externe Imports
from qt_material import apply_stylesheet

from PyQt6.QtWidgets import QApplication, QSplashScreen
from PyQt6.QtGui import QIcon, QPixmap


# Legacy imports
from shared.info import APP_ICON
from shared.logger import log
from main.main_window import MainWindow
from viewmodels.main_vm import MainViewModel


# The parent of appalication
class App(QApplication):
    def __init__(self, *args):
        super().__init__(*args)
        self.setWindowIcon(QIcon(APP_ICON))
        self.__applyThemes("dark_blue.xml")

    def __showSplash(self):
        self.splash = QSplashScreen(QPixmap(APP_ICON))
        self.splash.show()

    def __applyThemes(self, xmlTheme: str):
        log.debug(f" ############################## App uses Style: {xmlTheme} ---")
        apply_stylesheet(self, xmlTheme)

    def showMainWindow(self):
        log.info("##############################  App is Loading  ---")
        self.mainWindow = MainWindow(MainViewModel())
        # Show the main window
        self.mainWindow.show()
