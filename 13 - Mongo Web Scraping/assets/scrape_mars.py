# DEPENDENCIES
import pymongo
import flask import Flask, jsonify, request

## scrape function that will execute all of your scraping code
## from above and return one Python dictionary
## containing all of the scraped data.

# Route "/scrap" that will import 

# Root route "/" that will query Mongo Database and pass the mars
# data into an HTML template to display the data


app = Flask(__name__)

# BASIC (TEST) GET ROUTE
@app.route("/scrape", methods=["GET"])
def get_test():
    if request.method == "GET":
        return jsonify({"It is": "working!"})

# POST ROUTE
@app.route("/", methods=["POST"])
def posting():

    # Create a todo dictionary
    todo = {"todo": request.form["todo"],
            "priority": request.form["priority"]}

    # Return JSON
    return jsonify(todo)

if __name__ == '__main__':
    app.run(debug=False)

@app.route("/", methods=["GET"])
def get_test():
    if request.method == "GET":
        return jsonify


## STORE THE RETURN VALUE IN MONGO AS A PYTHON DICTIONARY

conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

# DEFINE THE CLASSDB DATABASE IN MONGO
db = client.classDB

classroom = db.classroom.find()

for student 

# USE PYMONGO FOR CRUD APPLICATIONS FOR YOUR DATABASE.
# INSERTMANY TO HTML


## CREATE A ROOT ROUTE "/" THAT WILL QUERY YOUR MONGO DATABASE AND PASS YOUR MARS DATA
## INTO AN HTML TEMPLATE TO DISPLAY THE DATA

@app.route("/", methods=["GET"])
def get_test():
    if request.method = "GET":
        return jsonify