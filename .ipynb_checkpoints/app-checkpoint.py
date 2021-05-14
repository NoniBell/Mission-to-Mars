# import necessary libraries
from flask import Flask, render_template

# create instance of Flask app
app = Flask(__name__)

# Create connection variable
conn = 'mongodb://localhost:27017'

# Pass connection to the pymongo instance.
client = pymongo.MongoClient(conn)

# Connect to a database. Will create one if not already available.
db = client.mars_db

#drop mars db is exists
db.mars.drop()

if __name__ == "__main__":
    app.run(debug=True)