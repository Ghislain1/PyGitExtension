# viewmodels/user_vm.py
from PyQt6.QtCore import QObject, pyqtSignal, pyqtProperty
from models.user_model import User


class UserViewModel(QObject):
    nameChanged = pyqtSignal(str)
    emailChanged = pyqtSignal(str)

    def __init__(self, user: User, data_service):
        super().__init__()
        self._user = user
        self._data_service = data_service

    @pyqtProperty(str, notify=nameChanged)
    def name(self):
        return self._user.name

    @name.setter
    def name(self, value):
        self._user.name = value
        self.nameChanged.emit(value)

    @pyqtProperty(str, notify=emailChanged)
    def email(self):
        return self._user.email

    @email.setter
    def email(self, value):
        self._user.email = value
        self.emailChanged.emit(value)
        self._data_service.save_user(self._user)
