from marshmallow import fields
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy


ma = Marshmallow()
db = SQLAlchemy()


class Persona(db.Model):
    __tablename__ = 'persona'
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    name = db.Column(db.String(250), nullable=False)
    surname = db.Column(db.String(250), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    creation_date = db.Column(db.TIMESTAMP,
                              server_default=db.func.current_timestamp(),
                              nullable=False)

    def __init__(self, id, name, surname, age):
        self.id = id
        self.name = name
        self.surname = surname
        self.age = age


class PersonaSchema(ma.Schema):
    id = fields.Integer(required=True)
    name = fields.String(required=False)
    surname = fields.String(required=False)
    age = fields.Integer(required=False)
    creation_date = fields.DateTime()
