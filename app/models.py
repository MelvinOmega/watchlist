from . import db
from werkzeug.security import generate_password_hash,check_password_hash
import app
from flask_login import UserMixin
from . import login_manager
class News:
    '''
    News class to define News Objects
    '''
    def __init__(self,id,name,url,description,category, country):
        self.id =id
        self.name= name
        self.url = url
        self.description = description
        self.category = category
        self.country = country
class Articles:
    get_articles = []
    def __init__(self,title,author,url,description, urlToImage, publishedAt, content):
        self.title = title
        self.author = author
        self.url = url
        self.description= description
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    pass_secure = db.Column(db.String(255))

    def __repr__(self):
        return f'User {self.username}'

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")

    def __repr__(self):
        return f'User {self.name}'        


    pass_secure  = db.Column(db.String(255))

    @property
    def password(self):
            raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password) 

class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    password_hash = db.Column(db.String(255)) 
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_secure = db.Column(db.String(255))

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
            




