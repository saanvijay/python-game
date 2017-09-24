from pymongo import MongoClient
from datetime import datetime
import getpass

# 27017 is the default port
client = MongoClient('mongodb://localhost:27017/')

# Create database
db = client.testdb


today = str(datetime.now())
username = getpass.getuser()

class scoreCollection:
	def putScore(self, score):
		db.highest_score.insert_one(
			{ "date" : today,
	  		"user" : username,
	  		"score": score
			}
		)
	def getHighestScore(self):
		sortlist = db.highest_score.find().sort("score", pymongo.ASCENDING)	
		return sortlist[0]
