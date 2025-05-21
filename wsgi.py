import sys
import os

# Import the app directly from main.py
from main import app as application

# For Gunicorn
app = application
