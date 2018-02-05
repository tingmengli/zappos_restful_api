from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item
from resources.menu import Menu
from resources.restaurant import Restaurant

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data2.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'tingmeng'
api = Api(app)

@app.before_first_request
def create_tables():
	db.create_all()
	print("created db")

jwt = JWT(app, authenticate, identity) # /auth

api.add_resource(Menu, '/menu/<int:menuid>')
api.add_resource(Item, '/item/<int:itemid>')
api.add_resource(Restaurant, '/restaurant/<int:restaurantid>')


api.add_resource(UserRegister, '/register')


if __name__ == '__main__':
	from db import db # to avoid circular import
	db.init_app(app) 
	app.run(port=5000, debug=True)