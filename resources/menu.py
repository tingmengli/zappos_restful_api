from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.menu import MenuModel

class Menu(Resource):
	parser = reqparse.RequestParser()
	parser.add_argument('name',
		required=True,
		help="Every menu needs a name."
	)
	parser.add_argument('restaurant_id',
		type=int,
		required=True,
		help="Every menu needs a restaurant id."
	)

	@jwt_required()
	def get(self, menuid):
		menu = MenuModel.find_by_id(menuid)
		if menu:
			return menu.json()
		return {'message': 'menu not found'}, 404

	def put(self, menuid):
		menu = MenuModel.find_by_id(menuid)
		data = Menu.parser.parse_args()
		if menu:
			menu.name = data['name']
			menu.restaurant_id = data['restaurant_id']
		else:
			menu = MenuModel(data['name'], data['restaurant_id'])

		try:
			menu.save_to_db()
		except:
			return {'message': 'An error occurred while creating the menu'}, 500

		return menu.json(), 201

	def delete(self, menuid):
		menu = MenuModel.find_by_id(menuid)
		if menu:
			menu.delete_from_db()

		return {'message': 'menu deleted'}

class CreateMenu(Resource):
	parser = reqparse.RequestParser()
	parser.add_argument('name',
		required=True,
		help="Every menu needs a name."
	)
	parser.add_argument('restaurant_id',
		type=int,
		required=True,
		help="Every menu needs a restaurant id."
	)
	def post(self):
		data = CreateMenu.parser.parse_args()
		menu = MenuModel(data['name'], data['restaurant_id'])

		try:
			menu.save_to_db()
		except:
			return {'message': 'An error occurred while creating the menu'}, 500

		return menu.json(), 201
