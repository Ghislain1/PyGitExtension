
# pip install --upgrade pytest pytest-qt PyQt6

import pytest
from PyQt6.QtWidgets import QWidget
from src.ui.main_window import MainWindow
 

@pytest.fixture
def window(qtbot):
    mainWindow = MainWindow() 
    try:
         qtbot.addWidget(mainWindow) # To Ensure that the widget gets closed by the end of the test
    except Exception as e:
        print(f"An error occurred: {e}")

    return mainWindow
 

# The prefix test_  is default naming convention for auto discovery.

def test_button_click(window):
     # Verify initial state
    # assert window.button.text() == "TODO!"
    pass

  
 