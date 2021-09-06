from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys




class DerWindow(QMainWindow):
    def __init__(self):
        super(DerWindow, self).__init__()
        self.setGeometry(800, 200, 300, 300)  #x,y,width,height
        self.setWindowTitle("Open Rice Bot 1.0")
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)  
        self.label.setText("My first label")
        self.label.move(50,50)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Click me")
        self.b1.clicked.connect(self.clickit)

    def clickit(self):
        self.label.setText("you clicked it!")
        self.update()

    def update(self):
        self.label.adjustSize()




def window():
    app = QApplication(sys.argv)
    win = DerWindow()




    win.show()
    sys.exit(app.exec_())

window()