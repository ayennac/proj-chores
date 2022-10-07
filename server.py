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

@app.route('/login', methods=['GET'])
def show_login():
    """Show login page"""
    return render_template("login.html")


@app.route('/user-login', methods=['POST'])
def login_user():
    """Login user"""
    username = request.json.get('username')
    password = request.json.get('password')
    potential_user = crud.get_user_by_username(username)

    if potential_user.password == password:
        session['user_id'] = potential_user.user_id
        flash('Logged in!')
    else:
        flash('Not logged in!')
    return jsonify({'code': 'result_code'})

if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)