
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel

# Student class inheritences from Resource class
class Item(Resource):
	parser = reqparse.RequestParser()
	parser.add_argument('name',
		required=True,
		help="Every item needs a name."
	)
	parser.add_argument('price',
		type=float,
		required=True,
		help="This field cannot be left blank."
	)
	parser.add_argument('menu_id',
		type=int,
		required=True,
		help="Every item needs a menu id."
	)


	@jwt_required()
	def get(self, itemid):
		item = ItemModel.find_by_id(itemid)
		if item:
			return item.json()

		return {'message': 'Item not found'}, 404

	def put(self, itemid):
		data = Item.parser.parse_args()

		item = ItemModel.find_by_id(itemid)

		if item is None:
			item =ItemModel(data['name'], data['price'], data['menu_id'])
		else:
			item.name = data['name']
			item.price = data['price']
			item.menu_id = data['menu_id']

		item.save_to_db()

		return item.json()

	def delete(self, itemid):
		item = ItemModel.find_by_id(itemid)
		if item:
			item.delete_from_db()

		return {'message': 'Item deleted'}


class CreateItem(Resource):
	parser = reqparse.RequestParser()
	parser.add_argument('name',
		required=True,
		help="Every item needs a name."
	)
	parser.add_argument('price',
		type=float,
		required=True,
		help="This field cannot be left blank."
	)
	parser.add_argument('menu_id',
		type=int,
		required=True,
		help="Every item needs a menu id."
	)
	def post(self):
		data = CreateItem.parser.parse_args()
		item = ItemModel(data['name'], data['price'], data['menu_id'])

		try:
			item.save_to_db()
		except:
			return {'message': 'An error occurred while creating the item'}, 500

		return item.json(), 201

		
