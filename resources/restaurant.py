from flask_restful import Resource, reqparse
from models.restaurant import RestaurantModel

class Restaurant(Resource):
	parser = reqparse.RequestParser()
	parser.add_argument('name',
		required=True,
		help="Every restaurant needs a name."
	)

	def get(self, restaurantid):
		restaurant = RestaurantModel.find_by_id(restaurantid)
		if restaurant:
			return restaurant.json()
		return {'message': 'restaurant not found'}, 404

	def put(self, restaurantid):
		restaurant = RestaurantModel.find_by_id(restaurantid)
		data = Restaurant.parser.parse_args()
		if restaurant:
			restaurant.name = data['name']
		else:
			restaurant = RestaurantModel(data['name'])
		try:
			restaurant.save_to_db()
		except:
			return {'message': 'An error occurred while creating the restaurant'}, 500

		return restaurant.json(), 201

	def delete(self, restaurantid):
		restaurant = RestaurantModel.find_by_id(restaurantid)
		if restaurant:
			restaurant.delete_from_db()

		return {'message': 'restaurant deleted'}

class RestaurantList(Resource):
	def get(self):
		return {'restaurants': [restaurant.json() for restaurant in RestaurantModel.query.all()]}

class CreateRestaurant(Resource):
	parser = reqparse.RequestParser()
	parser.add_argument('name',
		required=True,
		help="Every menu needs a name."
	)
	
	def post(self):
		data = CreateRestaurant.parser.parse_args()
		restaurant = RestaurantModel(data['name'])

		try:
			restaurant.save_to_db()
		except:
			return {'message': 'An error occurred while creating the restaurant'}, 500

		return restaurant.json(), 201


