from PyQt6.QtCore import QObject, pyqtSignal, pyqtProperty

from models.counter_model import CounterModel


class CounterViewModel(QObject):
    """Holds state, exposes properties & commands"""

    countChanged = pyqtSignal(int)

    def __init__(self, value: int = 0):
        super().__init__()
        self._model = CounterModel()

    @pyqtProperty(int, notify=countChanged)
    def count(self):
        return self._model.value()

    def increment(self):
        self._model.increment()
        self.countChanged.emit(self._model.value())
