

import pytest
from main_window import MainWindow

def test_window_title(qtbot):
    window = MainWindow()
    qtbot.addWidget(window)
    assert window.windowTitle == "PyGitExtension"