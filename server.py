from flask import Flask, url_for, redirect, request, jsonify
import mysql.connector
from mysql.connector import Error
import json

app = Flask(__name__, static_url_path='', static_folder='staticpages')

# Database configuration for WAMP/phpMyAdmin
DB_CONFIG = {
    'host': 'localhost',
    'database': 'expensedb',  # Replace with your actual database name
    'user': 'root',                 # Default WAMP username
    'password': '',                 # Default WAMP password (usually empty)
    'port': 3306
}

def get_db_connection():
    """Create and return a database connection"""
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        if connection.is_connected():
            print("Successfully connected to MySQL database")
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

def test_db_connection():
    """Test the database connection"""
    connection = get_db_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT 1")
            result = cursor.fetchone()
            print("Database connection test successful!")
            return True
        except Error as e:
            print(f"Database test failed: {e}")
            return False
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
    return False


@app.route('/')
def home():
    return "<h1>Server is running!</h1><a href='/test-db'>Test Database</a>"

@app.route('/test-db')
def test_database():
    connection = get_db_connection()
    if connection:
        connection.close()
        return "<h1>Database Connected Successfully!</h1>"
    else:
        return "<h1>Database Connection Failed!</h1>"

@app.route('/get-expenses')
def get_expenses():
    connection = get_db_connection()
    if not connection:
        return jsonify({'error': 'Database connection failed'})
    
    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM expenses")
        expenses = cursor.fetchall()
        return jsonify(expenses)
    except Exception as e:
        return jsonify({'error': str(e)})
    finally:
        if connection:
            cursor.close()
            connection.close()

if __name__ == "__main__":
    app.run(debug=True)