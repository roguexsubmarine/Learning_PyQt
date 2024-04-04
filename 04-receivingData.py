import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton



#your code starts here
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Check your terminal")

        button = QPushButton("Press Me!")

        # setting checkable property
        button.setCheckable(True)
        button.clicked.connect(self.the_button_was_clicked)
        button.clicked.connect(self.the_button_was_toggled)

        self.setCentralWidget(button)

    def the_button_was_clicked(self):
        print("Clicked!")

    def the_button_was_toggled(self, checked):
        print("Checked?", checked)
#your code ends here



app = QApplication([])

window = MainWindow()
window.show()

app.exec()