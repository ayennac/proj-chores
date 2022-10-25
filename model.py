"""Models for Moments App"""


from flask_sqlalchemy import SQLAlchemy



db = SQLAlchemy()


class User(db.Model):
    """A user"""

    __tablename__ = 'users'
    user_id = db.Column(db.Integer, 
                        autoincrement=True,
                        primary_key = True)
    username = db.Column(db.String)
    fname = db.Column(db.String)
    lname = db.Column(db.String)
    email = db.Column(db.String)
    password = db.Column(db.String)
    
    images = db.relationship("Image", back_populates="user")

    def __repr__(self):
        return f'<User user_id={self.user_id} username={self.username}>'



class Image(db.Model):
    """An image created by the user"""

    __tablename__ = 'images'

    image_id = db.Column(db.Integer,
                        autoincrement= True,
                        primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    description = db.Column(db.String)
    image_src = db.Column(db.String)
    alt_text = db.Column(db.String)

    submitted = db.Column(db.Boolean)
    submission_status = db.Column(db.String)
    public = db.Column(db.Boolean)

    user = db.relationship("User", back_populates="images")

    def __repr__(self):
        return f'<Image image_id={self.image_id} alt_text = {self.alt_text}>'

def connect_to_db(flask_app, db_uri="postgresql:///images", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)
    

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.
    connect_to_db(app, echo=False)
    
