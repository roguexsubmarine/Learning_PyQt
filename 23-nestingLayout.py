import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout
from PyQt6.QtGui import QPalette, QColor # to add colour to help us visualise layouts


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Nesting Layout")

        # layout1 will be outer layout
        # layout2 and layout3 will be inside layout1


        layout1 = QHBoxLayout()

        layout2 = QVBoxLayout()
        layout3 = QVBoxLayout()

        # verticle box
        layout2.addWidget(Color('red'))
        layout2.addWidget(Color('yellow'))
        layout2.addWidget(Color('purple'))

        # verticle box
        layout3.addWidget(Color('red'))
        layout3.addWidget(Color('purple'))


        # adding layouts to outer layout
        layout1.addLayout( layout2 )
        layout1.addWidget(Color('green'))
        layout1.addLayout( layout3 )

        widget = QWidget()
        widget.setLayout(layout1)
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