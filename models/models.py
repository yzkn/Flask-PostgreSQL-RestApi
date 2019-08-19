from datetime import datetime
from restapi.database import db


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False)
    role = db.Column(db.Integer, unique=False)

    def __init__(self, name, role):
        self.name = name
        self.role = role

    def __repr__(self):
        return '{{"class": "{}", "id": "{}", "name": "{}", "role": "{}"}}'.format(__class__.__name__, self.id, self.name, self.role)
