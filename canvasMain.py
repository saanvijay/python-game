
from PyQt4.QtGui import *
from PyQt4.QtCore import *

import sys
from canvas import *
from constants import *

if __name__ == '__main__':
	application = QApplication(sys.argv)
	canvas = gameCanvas()
	canvas.resize(GAME.CANVAS_WIDTH, GAME.CANVAS_HEIGHT)
	canvas.setStyleSheet('background:black')
	canvas.setWindowTitle('Python Game')
	canvas.show()
	application.exec_()
