from viewmodels.main_vm import MainViewModel
from views.splash.splash_screen import SplashScreen
from views.main.main_window import MainWindow

from qt_material import apply_stylesheet
from shared.info import APP_ICON
from shared.logger import log


class Application:
    def __init__(self, qt_app):
        self.qt_app = qt_app
        self.__applyThemes__("dark_blue.xml")
        self.splash = SplashScreen()
        self.main_window = MainWindow(MainViewModel())

    def run(self):
        self.splash.show()
        self.qt_app.processEvents()  # allow splash to paint
        # simulate loading (replace with real init)
        self.splash.finish(self.main_window)
        self.main_window.show()

    def __applyThemes__(self, xmlTheme: str):
        log.debug(f" ############################## App uses Style: {xmlTheme} ---")
        apply_stylesheet(self.qt_app, xmlTheme, invert_secondary=False)
