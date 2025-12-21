from PyQt6.QtCore import QObject, pyqtSignal, pyqtProperty
from qt_material import apply_stylesheet
from models.counter_model import CounterModel
from services.settings_service import SettingsService


class SettingsViewModel(QObject):
    """Holds state, exposes properties & commands"""

    countChanged = pyqtSignal(int)

    def __init__(self, settings_service: SettingsService) -> None:
        super().__init__()
        self._model = CounterModel()
        self.settings_service = settings_service

    @pyqtProperty(int, notify=countChanged)
    def count(self):
        return self._model.value()

    def change_theme(self, theme: str):
        # TODO@Ghis refactor to use Application method to change theme
        self.settings_service.apply_stylesheet(theme, invert_secondary=False)

        # Logic to change theme can be added here
        print(f"Changing theme to: {theme}")
        self.countChanged.emit(self._model.value())
