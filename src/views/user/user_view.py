# views/user/user_view.py
from PyQt6.QtWidgets import QWidget
from PyQt6.uic import loadUi


class UserView(QWidget):
    def __init__(self, vm):
        super().__init__()
        loadUi("views/user/user_view.ui", self)

        self.vm = vm
        self.btnSave.clicked.connect(lambda: self.vm.rename(self.txtName.text()))

        self.vm.userChanged.connect(self.lblName.setText)
