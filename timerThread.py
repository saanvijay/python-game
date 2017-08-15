#----------------- thread --------------
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import threading 
import sys

class timerGui(QWidget):
	def __init__(self, *args):
		QWidget.__init__(self, *args)
		self.seconds = 10
		self.count = 10
		self.timer = QTimer()
		self.timer.timeout.connect(self.counter, self.seconds)
		self.createWidget()
		
	def createWidget(self):
		counterLayout = QFormLayout()
		self.setLayout(counterLayout)
		timeRemaining = "Time Reamining {} seconds".format(self.count)
		reduceCountLabel = QLabel(timeRemaining)
		counterLayout.addWidget(reduceCountLabel)
		self.show()

	def counter(self):
		self.count -= 1
		print "count is", count
		if self.count == self.seconds:
			sys.exit()
		

