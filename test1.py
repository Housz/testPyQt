from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def window():
    app = QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(800, 600, 400, 400)
    win.setWindowTitle("test pyqt")

    win.show()
    sys.exit(app.exec_())

window()