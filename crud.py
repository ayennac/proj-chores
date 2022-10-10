"""CRUD operations"""

from model import db, Image, connect_to_db, User

from random import choice


def create_new_user(username, fname, lname, email, password):
    """Return a new User object"""
    user = User(username=username, fname=fname, lname =lname, email =email, password=password)
    return user

def get_user_by_user_id(user_id):
    """Return a user from user_id"""
    return User.query.filter(User.user_id ==user_id).first()

def get_all_users_images(user_id):
    """Return all images from a user"""
    return Image.query.filter(User.user_id ==user_id).all()

def get_all_images():
    """Return a list of images"""
    return Image.query.all()

def get_random_image():
    """Return a random image"""
    images = get_all_images()
    image_chosen = choice(images)
    return image_chosen

def get_image_by_image_id(image_id):
    """Return an image from image_id"""
    return Image.query.filter(Image.image_id ==image_id).first()

def get_all_users():
    """Return a list of list of users"""
    return User.query.all()
    
def get_user_by_username(username):
    """Return a user from username"""
    return User.query.filter(User.username == username).first()

def get_user_by_email(email):
    """Return a  user from email"""
    return User.query.filter(User.email == email).first()

def get_random_user():
    """Return a random user"""
    users = get_all_users()
    user_chosen = choice(users)
    return user_chosen

def create_new_image(user, description, image_src, alt_text, submitted, submission_status, public):
    image = Image(user=user,
                    description=description,
                    image_src=image_src,
                    alt_text=alt_text,
                    submitted=submitted,
                    submission_status=submission_status,
                    public=public)
    
    return image