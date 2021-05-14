# import necessary libraries
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

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

@app.route('/')
def index():
    # Store the entire team collection in a list
    teams = list(db.team.find())
    print(teams)

    # Return the template with the teams list passed in
    return render_template('index.html', teams=teams)



if __name__ == "__main__":
    app.run(debug=True)