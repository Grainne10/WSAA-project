from flask import Flask, url_for, redirect, request, jsonify
import mysql.connector
from mysql.connector import Error
import json
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_url_path='', static_folder='staticpages')
CORS(app)


# SQL Alchemy uses Python classes to represent database tables.
# It handles connection pooling, transaction, session management. We connect to MySQL using pymysqldriver and coonect to the expensedb using the local host.  
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/expensedb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#  this is SQL Alchemy model , it maps to the table in the database. Using to_dict, converts and Expense object into a dictionary, so it can be returned as JSON in an API response.
class Expense(db.Model):
    __tablename__ = 'expenses'
    id = db.Column(db.Integer, primary_key=True)
    month = db.Column(db.String(20), nullable=False)
    category = db.Column(db.String(20), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'month': self.month,
            'category': self.category,
            'amount': self.amount,
            'status': self.status
        }

# Define 4 routes for CRUD. This allows the front end perform the basic operation on the expenses table.
 
 #Fetches all te expense records
@app.route('/expenses', methods=['GET'])
def get_expenses():
    expenses = Expense.query.all()
    return jsonify([e.to_dict() for e in expenses])


#  Creates a new expense object and adds it to the database
@app.route('/expenses', methods=['POST'])
def create_expense():
    data = request.json
    new_expense = Expense(
        month=data['month'],
        category=data['category'],
        amount=data['amount'],
        status=data['status']
    )
    db.session.add(new_expense)
    db.session.commit()
    return jsonify({'message': 'Expense created', 'expense': new_expense.to_dict()}), 201 

# Finds an existing expense and updates its fields

@app.route('/expenses/<int:id>', methods=['PUT'])
def update_expense(id):
    data = request.json
    expense = Expense.query.get(id)
    if not expense:
        return jsonify({'error': 'Expense not found'}), 404
    
    expense.month = data['month']
    expense.category = data['category']
    expense.amount = data['amount']
    expense.status = data['status']
    db.session.commit()
    return jsonify({'message': 'Expense updated', 'expense': expense.to_dict()})

#Finds an existing expense and deletes its fields.
@app.route('/expenses/<int:id>', methods=['DELETE'])
def delete_expense(id):
    expense = Expense.query.get(id)
    if not expense:
        return jsonify({'error': 'Expense not found'}), 404
    
    db.session.delete(expense)
    db.session.commit()
    return jsonify({'message': f'Expense {id} deleted'})

if __name__ == "__main__":
    app.run(debug=True)