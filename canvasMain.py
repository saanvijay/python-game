from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys

class gameCanvas(QWidget):
	def __init__(self, *args):
		QWidget.__init__(self, *args)
		canvasLayout = QFormLayout()
		#canvasLayout.addWidget(QLabel('Welcome to Python game'))
		#self.setLayout(canvasLayout)

	def paintEvent(self, event):
		painter = QPainter(self)
		painter.setPen(QPen(QColor(255,0,0)))
		painter.setBrush(Qt.SolidPattern)
		painter.drawEllipse(10,10, 50, 50)


if __name__ == '__main__':
	application = QApplication(sys.argv)
	canvas = gameCanvas()
	canvas.resize(400, 300)
	canvas.show()
	application.exec_()
