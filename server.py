from flask import Flask, url_for, redirect, request, jsonify
import mysql.connector
from mysql.connector import Error
import json
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_url_path='', static_folder='staticpages')
CORS(app)
# # Database configuration for WAMP/phpMyAdmin
# DB_CONFIG = {
#     'host': 'localhost',
#     'database': 'expensedb',  # Replace with your actual database name
#     'user': 'root',                 # Default WAMP username
#     'password': '',                 # Default WAMP password (usually empty)
#     'port': 3306
# }

# def get_db_connection():
#     """Create and return a database connection"""
#     try:
#         connection = mysql.connector.connect(**DB_CONFIG)
#         if connection.is_connected():
#             print("Successfully connected to MySQL database")
#         return connection
#     except Error as e:
#         print(f"Error connecting to MySQL: {e}")
#         return None

# def test_db_connection():
#     """Test the database connection"""
#     connection = get_db_connection()
#     if connection:
#         try:
#             cursor = connection.cursor()
#             cursor.execute("SELECT 1")
#             result = cursor.fetchone()
#             print("Database connection test successful!")
#             return True
#         except Error as e:
#             print(f"Database test failed: {e}")
#             return False
#         finally:
#             if connection.is_connected():
#                 cursor.close()
#                 connection.close()
#     return False


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/expensedb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    month = db.Column(db.String(20), nullable=False)
    category = db.Column(db.String(50), nullable=False)
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

# Define 4 routes for CRUD

@app.route('/expenses', methods=['GET'])
def get_expenses():
    expenses = Expense.query.all()
    return jsonify([e.to_dict() for e in expenses])

@app.route('/expenses', methods=['POST'])
def create_expense():
    data = request.json
    new_expense = Expense(
        month=data['month']
        category=data['category']
        amount=data['amount']
        status=data['status']
    )
    db.session.add(new_expense)
    db.session.commit()
    return jsonify({'message': 'Expense created', 'expense': new_expense.to_dict()}), 201 

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