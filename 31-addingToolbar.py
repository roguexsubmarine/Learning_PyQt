import sys
from PyQt6.QtWidgets import (
    QMainWindow, QApplication,
    QLabel, QToolBar, QStatusBar
)
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtCore import Qt

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Toolbars")

        label = QLabel("  You can Move the toolbar by dragging it by the 3 dots  \n  you can right click and turn off it as well  \nHover on the button above and check \nthe Name beside the cursor and the Status on the bottom left of the window  \n n;)")

        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.setCentralWidget(label)
        toolbar = QToolBar("My main toolbar")
        self.addToolBar(toolbar)

        button_action = QAction("Your button", self)
        button_action.setStatusTip("This is your button")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True)
        toolbar.addAction(button_action)

        self.setStatusBar(QStatusBar(self))

    def onMyToolBarButtonClick(self, s):
        print("click", s)



app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()