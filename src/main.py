# Built-in imports
import sys

# Externe Imports


from PyQt6.QtWidgets import QApplication
from qt_material import apply_stylesheet

from viewmodels.main_vm import MainViewModel
from views.main.main_window import MainWindow

sys.path.append(".")


def main():
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme="dark_blue.xml")
    app.setApplicationName("PyGitExtension")

    # 2. Create the MainViewModel
    vm = MainViewModel()

    # 3. Create the MainView and pass the ViewModel
    window = MainWindow(vm)

    # 4. Show the window
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
