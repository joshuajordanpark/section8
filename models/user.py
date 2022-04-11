# import sqlite3
from db import db

class UserModel(db.Model):
    # sqlAlchemy creating table
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def save_to_db(self):
        db.session.add(self);
        db.session.commit();

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_email(cls, email):
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        #
        # query = "SELECT * FROM users WHERE email=?"
        # result = cursor.execute(query, (email,))
        # row = result.fetchone()
        # if row:
        #     user = cls(*row) # cls(row[0], row[1], row[2])
        # else:
        #     user = None
        #
        # connection.close()
        # return user
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_by_id(cls, _id):
        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        #
        # query = "SELECT * FROM users WHERE id=?"
        # result = cursor.execute(query, (_id,))
        # row = result.fetchone()
        # if row:
        #     user = cls(*row) # cls(row[0], row[1], row[2])
        # else:
        #     user = None
        #
        # connection.close()
        # return user
        return cls.query.filter_by(id=_id).first()
