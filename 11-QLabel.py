import sys

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QWidget,
)


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("QLabel")

        widget = QLabel("Hello")
        widget.setText("Center")
        font = widget.font()
        font.setPointSize(30)
        widget.setFont(font)

        # to set it to center !!!
        widget.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignVCenter)

        self.setCentralWidget(widget)

        


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
