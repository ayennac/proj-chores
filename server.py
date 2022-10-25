"""Server for chore buddy ."""

from flask import (Flask, render_template, request, flash, session,
                   redirect, jsonify)

import os
from jinja2 import StrictUndefined

import cloudinary.uploader

import crud

from model import connect_to_db, db, Image, User

import bcrypt

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

@app.route('/signup', methods=["GET"])
def show_signup():
    """Show sign up"""
    return render_template("signup.html")

@app.route('/user-signup', methods=['POST'])
def signup_user():
    """Sign up user"""

    fname = request.json.get('firstname')
    lname = request.json.get('lastname')
    username = request.json.get('username')
    email = request.json.get('email')
    password = request.json.get('signpassword')    
    try:
        if crud.get_user_by_email(email):
            result_code = False
        if crud.get_user_by_username(username):
            result_code = False
        else:
            new_user = crud.create_new_user(username, fname, lname, email, password)
            db.session.add(new_user)
            db.session.commit()
            flash("Account was made")
            result_code = True
    except AttributeError:
        result_code = False
    return jsonify({'code': result_code})

@app.route('/login', methods=['GET'])
def show_login():
    """Show login page"""
    return render_template("login.html")

@app.route('/user-login', methods=['POST'])
def login_user():
    """Login user"""
    username = request.json.get('username')
    password = request.json.get('password')
    password_encoded = password.encode('utf-8')

    try:
        potential_user = crud.get_user_by_username(username)
        print(potential_user.password)
        if bcrypt.checkpw(password_encoded,potential_user.password.encode('utf-8')):
            session['user_id'] = potential_user.user_id
            result_code = True
        else:
            result_code = False
    except AttributeError:
        result_code = False
    return jsonify({'code': result_code})

@app.route("/logout")
def process_logout():
    """Log user out."""

    del session["user_id"]
    flash("Logged out.")
    return redirect("/")

@app.route('/userprofile')
def show_user_profile():
    """Show user profile"""
    
    user_id = session.get('user_id')
    if not user_id:
        flash("please log in")
        return redirect('/login')

    user = crud.get_user_by_user_id(user_id)
    images = crud.get_all_users_images(user_id)

    return render_template('userprofile.html', 
                            user = user,
                            images = images)

                            
@app.route('/admin', methods=['GET'])
def show_admin():
    """Show login page"""
    images = crud.get_all_images()
    return render_template("admin.html", images = images)

@app.route('/new-image', methods=['POST'])
def new_image():
    user = crud.get_user_by_user_id(session.get('user_id'))
    img_src = request.files["input-img"]
    alt_text = request.form.get("alt-text")
    description = request.form.get("img-description")  
    submit_public = bool(request.form.get("img-submitted-public"))

    cloudinary_request = cloudinary.uploader.upload(img_src,
                                                    api_key=CLOUDINARY_KEY,
                                                    api_secret=CLOUDINARY_SECRET,
                                                    cloud_name=CLOUD_NAME,
                                                    resource_type = "video")
    cloudinary_img_src = cloudinary_request['secure_url']

    new_img = crud.create_new_image(user,
                                    description,
                                    cloudinary_img_src,
                                    alt_text,
                                    submit_public, 
                                    "Approved",
                                    True)
                
    db.session.add(new_img)    
    db.session.commit()
    flash("Added image to database!")
    return redirect("/userprofile")


@app.route('/edit-image', methods=['POST'])
def edit_image():
    user = crud.get_user_by_user_id(session.get('user_id'))
    image_id = request.form.get("edit-img-id")

    image = crud.get_image_by_image_id(image_id)
    alt_text = request.form.get("edit-alt-text")
    description = request.form.get("edit-img-description")
    #bool on a script will always make this submitted 
    submit_public = bool(request.form.get("edit-img-submitted"))
   
    image.description = description
    image.alt_text = alt_text
    image.submitted = submit_public

    db.session.commit()

    flash("Edited image in database!")

    return redirect("/userprofile")


@app.route('/admin-edit-status')
def admin_edit_status():
    image_id = request.args.get("image_id")
    image_approval = request.args.get("image_approval")

    image = crud.get_image_by_image_id(image_id)

    image.submission_status = image_approval

    db.session.commit()
    # Add logic on what happens to the public status if they do get approved

    result_code = True

    return jsonify({'code': result_code})


@app.route('/view-image')
def view_image():
    """JSON information about a single image"""
    image_id = request.args.get("image_id")
    image = crud.get_image_by_image_id(image_id)
    image_to_edit = [{"user": image.user_id,
                    "image_id": image.image_id,
                    "description": image.description,
                    "image_src": image.image_src,
                    "alt_text": image.alt_text,
                    "submitted": image.submitted,
                    "submission_status": image.submission_status,
                    "public":image.public
                    }] 
    return jsonify(image_to_edit)

@app.route('/view-mundane')
def view_random_image():
    """Return a random image for a viewer to idly watch"""
    random_image = crud.get_random_image()

    return render_template("view-mundane.html", random_image = random_image)





if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)

