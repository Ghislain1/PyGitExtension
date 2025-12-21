# views/user/user_view.py
from PyQt6.QtWidgets import QWidget
from PyQt6.uic import loadUi
from qt_material import list_themes

from viewmodels.settings_vm import SettingsViewModel


class SettingsView(QWidget):
    def __init__(self, vm):
        super().__init__()
        loadUi("views/settings/settings_view.ui", self)

        self.datacontext: SettingsViewModel = vm

        themes = list_themes()
        self.comboThemes.addItems(themes)
        self.comboThemes.setCurrentText("dark_blue.xml")

        # Connect UI elements to ViewModel commands/properties
        self.btnSaveSettings.clicked.connect(
            lambda: self.datacontext.rename(self.txtName.text())
        )

        self.comboThemes.currentTextChanged.connect(
            lambda theme: self.datacontext.change_theme(theme)
        )
