from PyQt4.QtGui import *
from PyQt4.QtCore import *

import sys
from random import randint
from constants import *
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
		self.ds = {}
		self.uscore = 0
		self.remainingSecs = GAME.REMAINING_SECONDS
		self.dialog = None
		self.scoreDialog()
		self.msgBox = None

	def scoreDialog(self):
		font = QFont()
		font.setFamily('Arial')
		font.setPointSize(GAME.TEXT_FONT_SIZE)
		self.dialog = QDialog()
		self.dialog.setFont(font)
		self.dialog.move(GAME.SCORE_DIALOG_POS_X,GAME.SCORE_DIALOG_POS_Y)
		self.dialog.resize(GAME.SCORE_DIALOG_WIDTH, GAME.SCORE_DIALOG_HEIGHT)
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
			self.gameOver()
		if self.current_count == self.count:
			self.timer.stop()
			self.current_count = 0
			self.update()
			self.timer.start(1000)
		
	def gameOver(self):
		self.msgBox = QMessageBox()
		self.msgBox.setText('GameOver')
		self.msgBox.setWindowTitle('GameOver')
		self.msgBox.setStyleSheet('background:darkCyan')
		self.msgBox.buttonClicked.connect(lambda:sys.exit())
		self.msgBox.show()


	def mousePressEvent(self, QMouseEvent):
		clickPos = QMouseEvent.pos()
		scoreCard = self.getScoreCard(QMouseEvent.x(), QMouseEvent.y())
		print "scoreCard", scoreCard
		print "dict.length", len(self.ds)
		if scoreCard == 0 :
			self.gameOver()
		self.uscore += scoreCard 
		self.dialog.close()
		self.scoreDialog()

	def mouseReleaseEvent(self, QMouseEvent):
		cursorPos = QCursor().pos()

	def getScoreCard(self, x, y):
		for rect,score in self.ds.iteritems():
			if x > rect.x() and x < rect.x() + GAME.REGION_X and y > rect.y() and y < rect.y() + GAME.REGION_Y :
					break;
		return score
		
	def paintEvent(self, event):
		del self.ds
		self.ds = dict()
		self.ds.clear()
		painter = QStylePainter(self)
		painter.setPen(QPen(QColor(255,0,0)))
		
		for i in xrange(GAME.POLYGONS_TO_GENERATE):
			painter.setBrush(QColor(randint(0,255),randint(0,255),randint(0,255)))
			xPos = randint(0, GAME.CANVAS_WIDTH - GAME.REGION_X)
			yPos = randint(0, GAME.CANVAS_HEIGHT - GAME.REGION_Y)
			rectangle = QRectF(int(xPos), int(yPos), int(GAME.REGION_X), int(GAME.REGION_Y))
			painter.drawEllipse(rectangle)
			txPos = xPos + GAME.SCORE_VALUE_POS_X
			tyPos = yPos + GAME.SCORE_VALUE_POS_Y
			painter.setPen(QPen(QColor(0,0,0)))
			scoreCard = randint(0,255)
			painter.drawText(int(txPos), int(tyPos), str(scoreCard))
			self.ds[rectangle] = scoreCard

	def center(self):
        	screen = QDesktopWidget().screenGeometry()
        	size = self.geometry()
        	self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)

