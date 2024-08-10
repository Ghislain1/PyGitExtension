

import sys
from PyQt6.QtWidgets import  QMainWindow




class MainWindow(QMainWindow):

    def __init__(self) -> None:    
        super().__init__()
        self.__setUi()

      

    def __setUi(self) -> None:

        self.setWindowTitle("PyGitExtension")
        self.setGeometry(100, 100, 600, 400)
         
     