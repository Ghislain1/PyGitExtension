

import pytest
from src.ui.main_window import MainWindow
 

@pytest.fixture
def window(qtbot):
    window = MainWindow()   
    qtbot.addWidget(window)
    return window


# The prefix test_  is default naming convention for auto discovery.
def test_window_title(window):
     
    assert window.windowTitle() == "PyGitExtension"