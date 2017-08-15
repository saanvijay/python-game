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
		self.uscore = 0
		self.remainingSecs = 60
		self.dialog = None
		self.scoreDialog()
		self.msgBox = None

	def scoreDialog(self):
		font = QFont()
		font.setFamily('Arial')
		font.setPointSize(15)
		self.dialog = QDialog()
		self.dialog.setFont(font)
		self.dialog.move(1200,120)
		self.dialog.resize(200,100)
		self.dialog.setWindowTitle('Score')
		self.dialog.setStyleSheet('background:green')
		self.dialog.layout = QFormLayout()
		self.dialog.setLayout(self.dialog.layout)
		txt = "score is {}".format(self.uscore)
		self.dialog.scoreLabel = QLabel(txt)
		self.dialog.layout.addWidget(self.dialog.scoreLabel)
		txt = "Remaining {} seconds".format(self.remainingSecs)
		self.dialog.rmLabel = QLabel(txt)
		self.dialog.layout.addWidget(self.dialog.rmLabel)
		self.dialog.show()


	def countMethod(self):
		self.current_count += 1
		self.remainingSecs -= 1
		if self.remainingSecs == 0:
			self.msgBox = QMessageBox()
			self.msgBox.setText('GameOver')
			self.msgBox.buttonClicked.connect(lambda:sys.exit())
			self.msgBox.show()
			#sys.exit()
		if self.current_count == self.count:
			self.timer.stop()
			self.current_count = 0
			self.update()
			self.timer.start(1000)
			self.ds = dict()
		

	def mousePressEvent(self, QMouseEvent):
		clickPos = QMouseEvent.pos()
		scoreCard = self.getScoreCard(QMouseEvent.x(), QMouseEvent.y())
		print "scoreCard", scoreCard
		self.uscore += scoreCard 
		self.dialog.close()
		self.scoreDialog()
	#	self.msg = QMessageBox()
###		txt = "your score is {}".format(self.uscore)
##		self.msg.setText(txt)
#		self.msg.show()


	def mouseReleaseEvent(self, QMouseEvent):
		cursorPos = QCursor().pos()

	def getScoreCard(self, x, y):
		for rect,score in self.ds.iteritems():
			if x > rect.x() and x < rect.x() + 50 and y > rect.y() and y < rect.y() + 50 :
					break;
		return score
		
	def paintEvent(self, event):
		painter = QStylePainter(self)
		#painter.begin(self)
		painter.setPen(QPen(QColor(255,0,0)))
		
		self.ds = dict()
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

