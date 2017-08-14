
from PyQt4.QtGui import *
from PyQt4.QtCore import *

import sys
from canvas import *
from timerThread import timerGui

if __name__ == '__main__':
	application = QApplication(sys.argv)
	canvas = gameCanvas()
	canvas.resize(800, 600)
	canvas.setStyleSheet('background:darkCyan')
	canvas.setWindowTitle('Python Game')
	canvas.show()
	application.exec_()
