"""Server for ghibli data viz ."""

from flask import (Flask, render_template, request, flash, session,
                   redirect, jsonify)

import os
from jinja2 import StrictUndefined

import cloudinary.uploader

# import crud

from model import connect_to_db, db, Image, User

app = Flask(__name__, template_folder='templates')
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


CLOUDINARY_KEY = os.environ['CLOUDINARY_KEY']
CLOUDINARY_SECRET = os.environ['CLOUDINARY_SECRET']
CLOUD_NAME = "dvrzkwd2m"

@app.route('/')
def show_homepage():
    """Show homepage"""

    return render_template("home.html")

if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)