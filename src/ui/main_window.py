

import sys
from PyQt6.QtWidgets import  QMainWindow, QVBoxLayout, QWidget, QPushButton




class MainWindow(QMainWindow):

    def __init__(self) -> None:    
        super().__init__()
        self.__setUi() # Call the private Method to init UI

      

    def __setUi(self) -> None:

        self.setWindowTitle("PyGitExtension")
        self.setGeometry(100, 100, 600, 400)
       
        self.button = QPushButton("TODO!")
        self.button.clicked.connect(self.on_button_click)

        layout = QVBoxLayout()
        layout.addWidget(self.button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)
        
         
    def on_button_click(self):
        self.button.setText("Clicked!")