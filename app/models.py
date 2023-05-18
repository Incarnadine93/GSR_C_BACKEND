from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash
db = SQLAlchemy()


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.String(400), unique=True, nullable=False)
    name = db.Column(db.String(400), unique=False, nullable=False)

    def __init__(self, uid, name):
        self.uid = uid
        self.name = name

    def create(self):
        db.session.add(self)
        db.session.commit()

    def to_dict(self):
        return {
            "id": self.id,
            "uid": self.uid,
            "name": self.name,
        }