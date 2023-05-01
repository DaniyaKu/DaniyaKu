import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from main import Ui_Narrator
from ans1 import Ui_Stanley
from ans2 import Ui_People
from ans3 import Ui_Robot
from last import Ui_Dialog


app = QtWidgets.QApplication(sys.argv)

Narrator = QtWidgets.QMainWindow()
ui = Ui_Narrator()
ui.setupUi(Narrator)
Narrator.show()


def openStanley():
	global Stanley
	Stanley = QtWidgets.QDialog()
	ui = Ui_Stanley()
	ui.setupUi(Stanley)
	Narrator.close()
	Stanley.show()

	
	def openDialog():
		global Dialog
		Dialog = QtWidgets.QDialog()
		ui = Ui_Dialog()
		ui.setupUi(Dialog)
		Stanley.close()
		Dialog.show()

	ui.pushButton.clicked.connect(openDialog)


ui.pushButton.clicked.connect(openStanley)

def openPeople():
	global People
	People = QtWidgets.QDialog()
	ui = Ui_People()
	ui.setupUi(People)
	Narrator.close()
	People.show()

	def returnTomain():
		People.close()
		Narrator.show()

	ui.pushButton.clicked.connect(returnTomain)

ui.pushButton_2.clicked.connect(openPeople)

def openRobot():
	global Robot
	Robot = QtWidgets.QDialog()
	ui = Ui_Robot()
	ui.setupUi(Robot)
	Narrator.close()
	Robot.show()

	def returnTomain():
		Robot.close()
		Narrator.show()

	ui.pushButton_4.clicked.connect(returnTomain)

ui.pushButton_3.clicked.connect(openRobot)

sys.exit(app.exec_())
