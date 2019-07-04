import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QFileDialog,QToolTip
from PyQt5.QtGui import QFont
from gui import *
class MyMainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        QToolTip.setFont(QFont("SansSerif",10))
        self.setToolTip("这是一个<b>测试提示</b>")
        self.setupUi(self)
        self.fileCloseAction.triggered.connect(self.close)
        self.fileOpenAction.triggered.connect(self.openMsg)
        self.toolButton.clicked.connect(self.openFile)
        self.toolButton_2.clicked.connect(self.openDirectory)
    def openMsg(self):
        file,ok=QFileDialog.getOpenFileName(self,"打开","./","All File (*);;Text Files (*.txt)")
        self.statusbar.showMessage(file,2000)


    def openFile(self):
        self.file, ok = QFileDialog.getOpenFileName(self, "保存文件路径", "./", "All File (*);;Text Files (*.txt)")
        self.lineEdit.setText(self.file)

    def openDirectory(self):
        self.file= QFileDialog.getExistingDirectory(self,"保存文件夹路径", "./")
        self.lineEdit_2.setText(self.file)

if __name__=="__main__":
    app=QApplication(sys.argv)
    myWin= MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())