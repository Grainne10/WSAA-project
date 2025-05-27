# WSAA-Project

## Expense Tracker


**by Grainne Boyle**



**README contents:**

1. [Overview](#overview)
2. [TechStack](#techstack)
3. [Project](#project)
4. [Research](#research)




## Overview

I am a student at the [Atlantic Technological University](https://www.atu.ie/), Galway, studying the Higher Diploma in Science in Data Analytics on a part-time basis over 2 years.  
This project is a simple web-based expense tracking application built with Flask (backend) and HTML/JavaScript (frontend).  
The application allows users to create, read, update, and delete expense records with categories, amounts, and status tracking. It demonstrates the following core concepts:  
Building a RESTful API with Flask.    
Connecting the API to a MySQL database via SQLAlchemy.    
Performing CRUD operations(Create, Read, UPdate,Delete) through the API and a simple web interface.    
Using AJAX to interact with the backend API from the frontend.  

## Tech Stack
### Backend:
Flask (Python web framework)
SQLAlchemy (ORM)
MySQL (Database)
Flask-CORS (Cross-origin resource sharing)
### Frontend:
HTML5
JavaScript (ES6+)
jQuery
CSS (basic styling)

## Project:

Prerequisites
Before running this application, make sure you have the following installed:

Python 3.12.4
MySQL Server
WAMP/XAMPP (recommended for local MySQL setup)

Installation
1. Clone the Repository  
git clone <WSAA-project>  
cd expense-viewer
2. Set Up Virtual Environment and activate  
python -m venv venv  
venv\Scripts\activate.bat  
3. Install Dependencies:  
install -r requirements.txt  
4. Database Setup  
Using WAMP/XAMPP:  
Start your WAMP server  
Open phpMyAdmin (usually at http://localhost/phpmyadmin)  
Create a new database named expensedb  
Create the expenses table:  
CREATE TABLE expenses (  
    id INT AUTO_INCREMENT PRIMARY KEY,  
    month VARCHAR(20) NOT NULL,  
    category VARCHAR(50) NOT NULL,  
    amount FLOAT NOT NULL,  
    status VARCHAR(20) NOT NULL  
);  

If you already have WAMP running and database set up:  

Just ensure your WAMP server is running (green icon in system tray).  
Verify that the expensedb database exists with the expenses table.  
The Flask application will automatically connect using the default WAMP settings (user = root, no password, localhost:3306).    

To run the Program:  

1. Open the Cmder console. In one console run python server.py  
The server will start on http://localhost:5000  

2. In second console , run python -m http.server. This Creates a local web server that serves files from the current directory and serves static files HTML, javascript.
Open http://localhost:8000/expense_viewer.html in your web browser. 

3. Usage - Go to the end of the sheet and fill in the expense form.
Adding Expenses: Fill out the form and click "Create an expense".  
Viewing Expenses: All expenses are displayed in the table automatically. They are auto incremented by ID as per your database table.  
Updating Expenses: Click the "Update" button next to any expense, modify the form, and submit.  
Deleting Expenses: Click the "Delete" button and confirm the deletion.  

4. For Pythonanywhere host - https://grainne10.pythonanywhere.com


## Research: 

1. [Courseware] - github.com Andrew Beatty courseware - Used templates for set up.     
2. [Config](https://stackoverflow.com/questions/39361115/git-ignore-accidentally-commited-file) - Removing file after commiting.     
3. [RestServer](https://stackoverflow.com/questions/58642563/what-is-difference-between-rest-api-and-rest-server) - Difference between rest api and restserver).      
4. [Ajax](https://www.geeksforgeeks.org/what-is-ajax/) - understanding what Ajax is.     
5. [Ajax](https://www.w3schools.com/xml/ajax_intro.asp) - how to use Ajax.  
6. [Jsonify](Use jsonify() instead of json.dumps() in Flask | GeeksforGeeks) - Use Jsonify.    
7. [HTML](HTML Tutorial) - Understanding html and writing html.  
8. [Python Anywhere](https://www.pythonanywhere.com/) - Hosting your application online.  
9. [CSS](https://www.geeksforgeeks.org/css-tutorial/) - Use of CSS styling in HTML , used Claude AI to provide code for styling.
10.[Image1] #Attributable picture :Expenses by http://www.nyphotographic.com/>Nick Youngson.   
 
END
 ![Expenses](Image1.jpg)