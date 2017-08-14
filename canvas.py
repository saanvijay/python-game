from PyQt4.QtGui import *
from PyQt4.QtCore import *

import sys
from random import randint

class gameCanvas(QWidget):
	def __init__(self, *args):
		QWidget.__init__(self, *args)
		canvasLayout = QFormLayout()
		self.setLayout(canvasLayout)
		self.center()
		self.count = 2
		self.current_count = 0
		self.timer = QTimer()
		self.timer.start(1000)
		self.timer.timeout.connect(self.countMethod)

	def countMethod(self):
		self.current_count +=1
		if self.current_count == self.count:
			self.timer.stop()
			self.current_count = 0
			self.update()
			self.timer.start(1000)
		

	def mousePressEvent(self, QMouseEvent):
		clickPos = QMouseEvent.pos()
		print "clickPos", clickPos

	def mouseReleaseEvent(self, QMouseEvent):
		cursorPos = QCursor().pos()
		print "cursorPos", cursorPos

	def paintEvent(self, event):
		painter = QStylePainter(self)
		#painter.begin(self)
		painter.setPen(QPen(QColor(255,0,0)))
		
		for i in xrange(20):
			painter.setBrush(QColor(randint(0,255),randint(0,255),randint(0,255)))
			xPos = randint(0,750)
			yPos = randint(0,550)
			painter.drawEllipse(xPos,yPos, 50, 50)
			txPos = xPos + 15
			tyPos = yPos + 30
			painter.setPen(QPen(QColor(0,0,0)))
			scoreCard = randint(0,255)
			painter.drawText(int(txPos), int(tyPos), str(scoreCard))
		#painter.end()
	def center(self):
        	screen = QDesktopWidget().screenGeometry()
        	size = self.geometry()
        	self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)

