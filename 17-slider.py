from PyQt5.QtWidgets import QMainWindow, QApplication, QSlider
from PyQt5.QtCore import Qt 
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Slider")

        widget = QSlider()

        widget.setMinimum(-10)
        widget.setMaximum(10)
        # Or: widget.setRange(-10,3)

        widget.setSingleStep(2) #in action when using keyboard

        ##orientation (verticle by default)
        # widget = QSlider(Qt.Orientiation.Vertical)
        # widget = QSlider(Qt.Orientiation.Horizontal)

        widget.valueChanged.connect(self.value_changed)
        widget.sliderMoved.connect(self.slider_position)
        widget.sliderPressed.connect(self.slider_pressed)
        widget.sliderReleased.connect(self.slider_released)

        self.setCentralWidget(widget)

    def value_changed(self, i):
        print(i)

    def slider_position(self, p):
        print("position", p)

    def slider_pressed(self):
        print("Pressed!")

    def slider_released(self):
        print("Released")



if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
