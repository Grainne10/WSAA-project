# Project for Web Services and Applications 

#**by Grainne Boyle**


# Created a virtual machine using python -m venv venv.
# This creates a venv folder enabling my project to safely install and run its own Python packages — without touching your global system Python.
if __name__ == '__main__':

from flask import Flask, request, jsonify, abort, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
#from expenseDAOskeleton import expenseDAO(set up files)

# Set up template 
app.route('/')

def home():

    return "Expense Tracker API"

 

@app.route('/expenses', methods=['GET'])

def get_expenses():

    return jsonify(expenseDAO.getAll())

 

@app.route('/expenses', methods=['POST'])

def add_expense():

    new_expense = request.json

    return jsonify(expenseDAO.create(new_expense))

 

# Create routes like PUT, DELETE...using Andrew'scode

 

if __name__ == '__main__':


from flask import Flask, request, jsonify, abort
from bookDAOskeleton import bookDAO

app = Flask(__name__)

@app.route('/')
def index():
        return "Hello world"

# getall
# curl http://127.0.0.1:5000/books

@app.route('/books', methods=['GET'])
def getall():
        return jsonify(bookDAO.getAll())

# find by id
# curl http://127.0.0.1:5000/books/1

@app.route('/books/<int:id>', methods=['GET'])
def findbyid(id):
        return jsonify(bookDAO.findByID(id))

#create
#curl -X POST -d "{\"title\":\"test\", \"author\":\"some guy\", \"price\":123}" http://127.0.0.1:5000/books
@app.route('/books', methods=['POST'])
def create():
        # read json from the body
        jsonstring = request.json
        book = {}

        if "title" not in jsonstring:
                abort(403)
        book["title"] = jsonstring["title"]
        if "author" not in jsonstring:
                abort(403)
        book["author"] = jsonstring["author"]
        if "price" not in jsonstring:
                abort(403)
        
        book["price"] = jsonstring["price"]
        
        return jsonify(bookDAO.create(book))

# update
# curl -X PUT -d "{\"title\":\"test\", \"author\":\"some guy\", \"price\":123}" http://127.0.0.1:5000/books/1

@app.route('/books/<int:id>', methods=['PUT'])
def update(id):
        jsonstring = request.json
        book = {}

        if "title" in jsonstring:
                book["title"] = jsonstring["title"]
        if "author" in jsonstring:
                book["author"] = jsonstring["author"]
        if "price" in jsonstring:
                book["price"] = jsonstring["price"]
        
        return jsonify(bookDAO.update(id, book))

# Delete
# curl -X DELETE  http://127.0.0.1:5000/books/1

@app.route('/books/<int:id>', methods=['DELETE'])
def delete(id):
        return jsonify(bookDAO.delete(id))

