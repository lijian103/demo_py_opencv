import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QMessageBox, QApplication, QPushButton, QDesktopWidget
from PyQt5.QtCore import QCoreApplication

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle("UEG")
        self.setWindowIcon(QIcon("./1.JPG"))

        qbtn = QPushButton("Quit", self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.setToolTip("This is a <b>QPushButon</b> widget")
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(50, 50)

        self.center()
        self.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, "Quit", "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myMainWindow = MainWindow()
    sys.exit(app.exec_())