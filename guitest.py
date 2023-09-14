from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QWidget()
    widget.resize(900, 700)
    widget.move(550, 180)
    widget.setWindowTitle("HH Parser")
    widget.show()
    
    
    sys.exit(app.exec_())

