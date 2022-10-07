"""Script to seed database."""

import os
import json

import model
import server

import crud

os.system("dropdb images")
os.system('createdb images')

model.connect_to_db(server.app)
model.db.create_all()

def get_dummy_users():
    """Load dummy users from dummy_users file"""
    with open('data/dummy_user.json') as f:
        user_data = json.loads(f.read())
        for user in user_data:
            new_user = crud.create_new_user(user["username"],
                                            user["fname"],
                                            user["lname"],
                                            user["email"],
                                            user["password"])
            model.db.session.add(new_user)
    model.db.session.commit()

def get_dummy_images():
    """Load dummy locations from dataset into database."""
    with open('data/dummy_image.json') as r:
        image_data = json.loads(r.read())
        for image in image_data:
            random_user = crud.get_random_user()
            new_image = crud.create_new_image(random_user,
                                                image['description'],
                                                image['image_src'],
                                                image['alt_text'],
                                                False, 
                                                "Approved",
                                                True)    
            model.db.session.add(new_image)    
    model.db.session.commit()
            


if __name__ == '__main__':
    model.connect_to_db(server.app)
    model.db.create_all()
    get_dummy_users()
    get_dummy_images()
