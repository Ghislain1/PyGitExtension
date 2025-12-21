from PyQt6.QtCore import QObject, pyqtSignal, pyqtProperty
from core.models import CounterModel


class LoginViewModel(QObject):
    usernameChanged = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self._username = ""

    @pyqtProperty(str, notify=usernameChanged)
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        self._username = value
        self.usernameChanged.emit(value)
