from PyQt5.QtWidgets import QMainWindow, QApplication, QSpinBox, QDoubleSpinBox
from PyQt5.QtCore import Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Spin Boxes")

        widget = QSpinBox()

        # # Or: widget = QDoubleSpinBox()
        # widget = QDoubleSpinBox()

        widget.setMinimum(-10)
        widget.setMaximum(6)
        # Or: widget.setRange(-10,3)

        widget.setPrefix("$")
        widget.setSuffix("c")
        widget.setSingleStep(3)  
        
        ## Or e.g. 0.5 for QDoubleSpinBox
        # widget.setSingleStep(0.5)
        
        widget.valueChanged.connect(self.value_changed)
        widget.textChanged.connect(self.value_changed_str)

        self.setCentralWidget(widget)

    def value_changed(self, i):
        print(i)

    def value_changed_str(self, s):
        print(s)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
