from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from datetime import datetime

# Initialize Flask app
app = Flask(__name__)

# Configurations
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///contact_messages.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize extensions
db = SQLAlchemy(app)
mail = Mail(app)

# Home route
@app.route('/')
def home():
    return render_template('home.html')

# Global template variables
@app.context_processor
def inject_globals():
    return {
        "site_name": "Ninestars Limited",
        "current_year": datetime.now().year
    }

# Import views (routes) at the end to avoid circular imports
from ninestars_website import views
