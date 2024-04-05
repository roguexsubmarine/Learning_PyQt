import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton



#your code starts here
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("My App")


        # add code here












app = QApplication([]) 
# #can also do 
# app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()