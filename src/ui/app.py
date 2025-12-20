# Externe Imports
from qt_material import apply_stylesheet

from PyQt6.QtWidgets import QApplication, QSplashScreen
from PyQt6.QtGui import QIcon, QPixmap


# Legacy imports

from core.info import APP_ICON
from ui.main_window import MainWindow

from core.logger import log


# The parent of appalication
class App(QApplication):
    def __init__(self, *args):
        super().__init__(*args)
        self.setWindowIcon(QIcon(APP_ICON))

    def __showSplash(self):
        self.splash = QSplashScreen(QPixmap(APP_ICON))
        self.splash.show()

    def __applyThemes(self, xmlTheme: str):
        log.debug(f" ############################## App uses Style: {xmlTheme} ---")
        apply_stylesheet(self, xmlTheme)

    def showMainWindow(self):
        log.info("##############################  App is Loading  ---")
        self.mainWindow = MainWindow()
        self.mainWindow.show()
