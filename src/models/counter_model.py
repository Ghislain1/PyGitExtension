class CounterModel:
    def __init__(self):
        self._count = 0

    def increment(self):
        self._count += 1

    def value(self) -> int:
        return self._count
