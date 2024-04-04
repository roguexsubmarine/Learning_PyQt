import sys
from PyQt6.QtWidgets import QApplication, QDialog, QMainWindow, QPushButton, QWidget, QHBoxLayout, QMessageBox



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Dialog Types")

        layout = QHBoxLayout()

        widget = QPushButton("Question")
        widget.clicked.connect(self.question_dialog)
        widget.setCheckable(False)
        layout.addWidget(widget)

        widget = QPushButton("Information")
        widget.clicked.connect(self.information_dialog)
        widget.setCheckable(False)
        layout.addWidget(widget)

        widget = QPushButton("Warning")
        widget.clicked.connect(self.warning_dialog)
        widget.setCheckable(False)
        layout.addWidget(widget)

        widget = QPushButton("Critical")
        widget.clicked.connect(self.critical_dialog)
        widget.setCheckable(False)
        layout.addWidget(widget)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


    def question_dialog(self):
        button = QMessageBox.question(
            self,
            "question",
            "answer the question '? ? ?'",
            buttons=QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Save | QMessageBox.StandardButton.Cancel,
            defaultButton=QMessageBox.StandardButton.Save,
        )
        if button == QMessageBox.StandardButton.Ok:
            print("Ok")
        else:
            print("not Ok")

    def information_dialog(self):
        button = QMessageBox.information(
            self,
            "informative",
            "Some Information",
            buttons=QMessageBox.StandardButton.Reset | QMessageBox.StandardButton.Abort | QMessageBox.StandardButton.Retry | QMessageBox.StandardButton.SaveAll,
            defaultButton=QMessageBox.StandardButton.Retry,
        )
        if button == QMessageBox.StandardButton.Retry:
            print("retry")
        else:
            print("not retry")

    def warning_dialog(self):
        button = QMessageBox.warning(
            self,
            "warning",
            "some warning ! ! !",
            buttons=QMessageBox.StandardButton.Ignore | QMessageBox.StandardButton.Discard | QMessageBox.StandardButton.RestoreDefaults,
            defaultButton=QMessageBox.StandardButton.Ignore,
        )
        if button == QMessageBox.StandardButton.Discard:
            print("Discard")
        else:
            print("Not Discard")
            
    def critical_dialog(self):
        button = QMessageBox.critical(
            self,
            "Oh dear!",
            "Something went very wrong.",
            buttons=QMessageBox.StandardButton.Discard | QMessageBox.StandardButton.NoToAll | QMessageBox.StandardButton.Ignore,
            defaultButton=QMessageBox.StandardButton.Discard,
        )
        self.buttonClicked = button
        if button == QMessageBox.StandardButton.Discard:
            print("Discard")
        else:
            print("Not Discard")



app = QApplication([])

window = MainWindow()
window.show()

sys.exit(app.exec())
