
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel

# Student class inheritences from Resource class
class Item(Resource):
	parser = reqparse.RequestParser()
	parser.add_argument('price',
		type=float,
		required=True,
		help="This field cannot be left blank."
	)
	# parser.add_argument('menu_id',
	# 	type=int,
	# 	required=True,
	# 	help="Every item needs a menu id."
	# )

	@jwt_required()
	def get(self, _id):
		item = ItemModel.find_by_id(_id)
		if item:
			return item.json()

		return {'message': 'Item not found'}, 404

	def post(self, _id):
		if ItemModel.find_by_id(_id):
			return {'message': "An item with name '{}' already exists.".format(name)}, 400

		data = Item.parser.parse_args()
		item = ItemModel(name, data['price'], data['menu_id'])

		# deal with exceptions
		try:
			item.save_to_db()
		except:
			return {"message": "An error occurred inserting the item."}, 500
			# internal serverl error 500

		return item.json(), 201

	def delete(self, _id):
		item = ItemModel.find_by_id(_id)
		if item:
			item.delete_from_db()

		return {'message': 'Item deleted'}

	def put(self, name):
		data = Item.parser.parse_args()

		item = ItemModel.find_by_id(_id)

		if item is None:
			item =ItemModel(name, data['price'], data['menu_id'])
		else:
			item.price = data['price']
			item.menu_id = data['menu_id']

		item.save_to_db()

		return item.json()

		
