
# Built-in imports
import sys

# Externe Imports
 
from qt_material import apply_stylesheet

from  ui.app import App
sys.path.append(".")  



def main ():
       
    app = App(sys.argv) 

    app.__showMainWindow()
     
    sys.exit(app.exec())

  

if __name__ == "__main__":
    main()