import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegister(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('email',
        type=str,
        required=True,
        help="This field cannot be left blank."
    )

    parser.add_argument('password',
        type=str,
        required=True,
        help="This field cannot be left blank."
    )

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_email(data['email']):
            return {"message": "A user with that email already exists"}, 400

        # connection = sqlite3.connect('data.db')
        # cursor = connection.cursor()
        #
        # query = "INSERT INTO users VALUES (NULL, ?, ?)"
        # cursor.execute(query, (data['email'], data['password']))
        #
        # connection.commit()
        # connection.close()

        # user = UserModel(data['username'], data['password'])
        user = UserModel(**data) # because of the parser, our data object will always have the two required parameters
        user.save_to_db()

        return {"message": "User created successfully."}, 201
