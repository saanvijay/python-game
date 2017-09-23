from pymongo import MongoClient
from datetime import datetime
import getpass

# 27017 is the default port
client = MongoClient('mongodb://localhost:27017/')

# Create database
db = client.testdb


today = str(datetime.now())
username = getpass.getuser()
# Insert simple data into collection
db.highest_score.insert_one(
	{ "date" : today,
	  "user" : username,
	  "score": "150"
	}
)
