from . import db
from sqlalchemy.sql import func

class Pay(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pay = db.Column(db.Integer)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
