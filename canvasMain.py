from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys

class gameCanvas(QWidget):
	def __init__(self, *args):
		QWidget.__init__(self, *args)
		canvasLayout = QFormLayout()
		canvasLayout.addWidget(QLabel('Welcome to Python game'))
		self.setLayout(canvasLayout)

	def paintEvent(self, event):
		painter = QPainter()
		painter.drawEllipse(10,10, 10, 10)

	

if __name__ == '__main__':
	application = QApplication(sys.argv)
	canvas = gameCanvas()
	canvas.resize(400, 300)
	canvas.show()
	application.exec_()
