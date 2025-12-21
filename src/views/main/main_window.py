from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QPushButton
from PyQt6.uic import loadUi
from viewmodels.main_vm import MainViewModel
from views.counter.counter_view import CounterView


class MainWindow(QMainWindow):
    def __init__(self, vm: MainViewModel) -> None:
        super().__init__()
        loadUi("views/main/mainwindow.ui", self)  # Load .ui
        self.vm = vm
        # counterPlaceholder is the QWidget you added in Designer
        layout = QVBoxLayout()
        self.counterPlaceholder.setLayout(layout)

        # Create CounterView and embed it
        self.counter_view = CounterView(self.vm.counter_vm)
        layout.addWidget(self.counter_view)

    def __setUi(self) -> None:
        self.setWindowTitle("PyGitExtension")
        self.setGeometry(100, 100, 600, 400)

        self.button = QPushButton("TODO!")
        self.button.clicked.connect(self.on_button_click)

        container = QWidget()
        # container.setLayout(layout)
        self.setCentralWidget(container)

    def on_button_click(self):
        self.button.setText("Clicked!")
