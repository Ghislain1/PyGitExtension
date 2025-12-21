from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout

from viewmodels.count_vm import CounterViewModel


class CounterView(QWidget):
    def __init__(self, vm: CounterViewModel):
        super().__init__()

        self.vm = vm

        self.label = QLabel()
        self.button = QPushButton("Increment1")

        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        # Bind UI → ViewModel
        self.button.clicked.connect(self.vm.increment)

        # Bind ViewModel → UI
        self.vm.countChanged.connect(self.update_label)

        # Initial state
        self.update_label(self.vm.count)

    def update_label(self, value: int):
        self.label.setText(f"Count: {value}")
