from PyQt4.QtGui import *
from PyQt4.QtCore import *

import sys
from random import randint

class gameCanvas(QWidget):
	def __init__(self, *args):
		QWidget.__init__(self, *args)
		canvasLayout = QFormLayout()
		self.setLayout(canvasLayout)
		self.timer = QTimer()
		self.timer.start(100)

	def mousePressEvent(self, QMouseEvent):
		clickPos = QMouseEvent.pos()
		print "clickPos", clickPos

	def mouseReleaseEvent(self, QMouseEvent):
		cursorPos = QCursor().pos()
		print "cursorPos", cursorPos

	def paintEvent(self, event):
		painter = QPainter(self)
		painter.setPen(QPen(QColor(255,0,0)))
		
		for i in xrange(255):
			self.timer.start(100)
			painter.setBrush(QColor(randint(0,255),randint(0,255),randint(0,255)))
			xPos = randint(0,750)
			yPos = randint(0,550)
			painter.drawEllipse(xPos,yPos, 50, 50)
			txPos = xPos + 15
			tyPos = yPos + 30
			painter.setPen(QPen(QColor(0,0,0)))
			painter.drawText(int(txPos), int(tyPos), str(i))
			self.timer.stop()

if __name__ == '__main__':
	application = QApplication(sys.argv)
	canvas = gameCanvas()
	canvas.resize(800, 600)
	canvas.setStyleSheet('background:darkCyan')
	canvas.setWindowTitle('Python Game')
	canvas.show()
	application.exec_()
