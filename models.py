from flask_sqlalchemy import SQLAlchemy
from werkzeug import generate_password_hash, check_password_hash
#importing the SQLAlchemy and Password classes

db = SQLAlchemy()
#creates a new usable instance from SQLAlchemy
class User(db.Model):
    __tablename__ = 'users'
    uid = db.Column(db.Integer, primary_key = True)
    firstname = db.Column(db.String(100))
    lastname = db.Column(db.String(100))
    email = db.Column(db.String(120), unique=True)
    pwdhash = db.Column(db.String(100))
#create a model that mirrors our DB and how it's setup  
    def __init__(self, firstname, lastname, email, password):
        self.firstname = firstname.title() #title makes the 1st letter uppercase
        self.lastname = lastname.title()
        self.email = email.lower() #makes it all lower case
        self.set_password(password) #this runs the set_password function and passes password to it
 #creates construtor that sets all the class's attributes       
    def set_password(self, password):
        self.pwdhash = generate_password_hash(password) #imported this on line 2        
    def check_password(self, password):
        return check_password_hash(self.pwdhash, password)