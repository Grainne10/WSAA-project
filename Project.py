# Project for Web Services and Applications 

#**by Grainne Boyle**


# Created a virtual machine using python -m venv venv.
# This creates a venv folder enabling my project to safely install and run its own Python packages — without touching your global system Python.


from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS