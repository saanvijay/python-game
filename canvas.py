from PyQt4.QtGui import *
from PyQt4.QtCore import *

import sys
from random import randint
#from timerThread import timerGui

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
		self.ds = dict()
		self.dialog = None

	def countMethod(self):
		self.current_count +=1
		if self.current_count == self.count:
			self.timer.stop()
			self.current_count = 0
			self.update()
			self.timer.start(1000)
			self.ds.clear()
		

	def mousePressEvent(self, QMouseEvent):
		clickPos = QMouseEvent.pos()
		print "clickPos", QMouseEvent.x()
		print "clickPos", QMouseEvent.y()
		clickedRegion = QRectF(int(QMouseEvent.x()), int(QMouseEvent.y()), int(50), int(50))
		print clickedRegion
		#print self.ds[clickedRegion]

	def mouseReleaseEvent(self, QMouseEvent):
		cursorPos = QCursor().pos()
		print "rclickPos", QMouseEvent.x()
		print "rclickPos", QMouseEvent.y()
		clickedRegion = QRectF(int(QMouseEvent.x()), int(QMouseEvent.y()), int(50), int(50))
		#print "cursorPos", cursorPos
		print self.getScoreCard(QMouseEvent.x(), QMouseEvent.y())

	def getScoreCard(self, x, y):
		for rect,score in self.ds.iteritems():
			if x > rect.x() and x < rect.x() + 50 and y > rect.y() and y < rect.y() + 50 :
					break;
		return score
		
	def paintEvent(self, event):
		painter = QStylePainter(self)
		#painter.begin(self)
		painter.setPen(QPen(QColor(255,0,0)))
		
		for i in xrange(20):
			painter.setBrush(QColor(randint(0,255),randint(0,255),randint(0,255)))
			xPos = randint(0,750)
			yPos = randint(0,550)
			#painter.drawEllipse(xPos,yPos, 50, 50)
			rectangle = QRectF(int(xPos), int(yPos), int(50), int(50))
			painter.drawEllipse(rectangle)
			txPos = xPos + 15
			tyPos = yPos + 30
			painter.setPen(QPen(QColor(0,0,0)))
			scoreCard = randint(0,255)
			painter.drawText(int(txPos), int(tyPos), str(scoreCard))
			self.ds[rectangle] = scoreCard
		#painter.end()
	def center(self):
        	screen = QDesktopWidget().screenGeometry()
        	size = self.geometry()
        	self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)

