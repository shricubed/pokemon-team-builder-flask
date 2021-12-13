from flask_login import UserMixin
from datetime import datetime
from . import db, login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.objects(username=user_id).first()

def get_team(user_id):
    return Team.objects(trainer=user_id).first()


class User(db.Document, UserMixin):

    email = db.EmailField(unique=True, required=True)
    username = db.StringField(unique=True, required=True)
    password = db.StringField()
    profile_pic = db.ImageField(required=False)

    # Returns unique string identifying our object
    def get_id(self):
        return self.username


class Team(db.Document):

    poster = db.ReferenceField(User)
    p1 = db.StringField(min_length=1, max_length=11, required=True)
    p2 = db.StringField(min_length=1, max_length=11, required=True)
    p3 = db.StringField(min_length=1, max_length=11, required=True)
    p4 = db.StringField(min_length=1, max_length=11, required=True)
    p5 = db.StringField(min_length=1, max_length=11, required=True)
    p6 = db.StringField(min_length=1, max_length=11, required=True)

class Comment(db.Document):
    commenter = db.ReferenceField(User)
    content = db.StringField(min_length=5, max_length=500, required=True)
    date = datetime.now()
    poster = db.StringField()





