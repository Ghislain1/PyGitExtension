from services.settings_service import SettingsService
from viewmodels.main_vm import MainViewModel
from views.splash.splash_screen import SplashScreen
from views.main.main_window import MainWindow

from qt_material import apply_stylesheet
from shared.info import APP_ICON
from shared.logger import log


class Application:
    def __init__(self, qt_app):
        self.qt_app = qt_app
        # self.qt_app.setWindowIcon(QIcon(APP_ICON))
        self.settings_service = SettingsService(self.qt_app)
        self.__applyThemes__("dark_blue.xml")
        self.splash = SplashScreen()
        self.main_window = MainWindow(MainViewModel(self.settings_service))

    def run(self):
        self.splash.show()
        self.qt_app.processEvents()  # allow splash to paint
        # simulate loading (replace with real init)
        self.splash.finish(self.main_window)
        self.main_window.show()

    def __applyThemes__(self, xmlTheme: str):
        log.debug(f" ############################## App uses Style: {xmlTheme} ---")
        self.settings_service.apply_stylesheet(xmlTheme)
