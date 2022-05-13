from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtGui import * 
from PyQt5.QtCore import QCoreApplication
import sys

# Creates a window
if __name__ == "__main__":
	app = QApplication(sys.argv)
	win = QMainWindow()
	win.setGeometry(200, 200, 1200, 800)
	win.setWindowTitle("Neuron")

# When button check is clicked
def clicked():
    try:
        if(1==1):
            lbl_cd.setText("Cat")
            lbl_cd.adjustSize()
    except:
        print('ERROR: An error occurred')

# Label "Welcome to neuron"
label = QtWidgets.QLabel(win)
label.setText("Welcome to neuron!")
label.setFont(QFont('Arial', 23))
label.adjustSize()
label.move(465,50)

# Button to start checking (JUST IN THIS DEMO)
button = QtWidgets.QPushButton(win)
button.setText("Start checking")
button.clicked.connect(clicked)
button.resize(100,32)
button.move(550,650)

# Label "Is an:"
lbl_is = QtWidgets.QLabel(win)
lbl_is.setText("Is an: ")
lbl_is.setFont(QFont('Arial', 15))
lbl_is.adjustSize()
lbl_is.move(500,350)

# Label "Cat or Dog"
lbl_cd = QtWidgets.QLabel(win)
lbl_cd.setText("?")
lbl_cd.setFont(QFont('Arial', 15))
lbl_cd.adjustSize()
lbl_cd.move(555,350)

# Button to close
button = QtWidgets.QPushButton(win)
button.setText("Close")
button.clicked.connect(QCoreApplication.instance().quit)
button.resize(100,32)
button.move(550,750)


###################
# Show the window
win.show()
sys.exit(app.exec_())

