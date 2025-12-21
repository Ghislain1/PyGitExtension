from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QLabel, QWidget
from PyQt6 import uic
from viewmodels.main_vm import MainViewModel
from views.counter.counter_view import CounterView
from views.settings.settings_view import SettingsView


class MainWindow(QMainWindow):
    def __init__(self, mainViewModel: MainViewModel) -> None:
        super().__init__()
        uic.loadUi("views/main/mainwindow.ui", self)  # Load .ui
        self.mainViewModel = mainViewModel

        self.setUpHomeView()
        self.setUpCounterView()
        self.setUpSettingsView()
        self.contentArea.setCurrentIndex(0)

    # TODO: Connect buttons to switch views REfactor to avoid duplicates
    def setUpHomeView(self):
        self.home_view = QLabel("Welcome to the Home View")
        # Add views to the stacked widget
        self.contentArea.addWidget(self.home_view)
        # Connect button to switch to counter view
        self.btnCounter.clicked.connect(lambda: self.contentArea.setCurrentIndex(0))

    def setUpCounterView(self):
        self.counter_view = CounterView(self.mainViewModel.counter_vm)
        # Add views to the stacked widget
        self.contentArea.addWidget(self.counter_view)
        # Connect button to switch to counter view
        self.btnCounter.clicked.connect(lambda: self.contentArea.setCurrentIndex(1))

    def setUpSettingsView(self):
        self.settings_view = SettingsView(self.mainViewModel.settings_vm)
        # Add views to the stacked widget
        self.contentArea.addWidget(self.settings_view)
        # Connect button to switch to counter view
        self.btnSettings.clicked.connect(lambda: self.contentArea.setCurrentIndex(2))
