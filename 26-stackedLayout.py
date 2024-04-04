import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QStackedLayout
from PyQt6.QtGui import QPalette, QColor # to add colour to help us visualise layouts


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Stacked Layout")

        layout = QStackedLayout()

        layout.addWidget(Color("red"))
        layout.addWidget(Color("green"))
        layout.addWidget(Color("blue"))
        layout.addWidget(Color("yellow"))


        # setting current top layer
        # it is exactly how tabbed views in applications work. 
        # Only one view ('tab') is visible at any one time.
        layout.setCurrentIndex(2)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)



class Color(QWidget):

    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)





app = QApplication([])
window = MainWindow()
window.show()

app.exec()