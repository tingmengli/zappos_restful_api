from flask_restful import Resource
from models.restaurant import RestaurantModel

class Restaurant(Resource):
	def get(self, name):
		restaurant = RestaurantModel.find_by_name(name)
		if restaurant:
			return restaurant.json()
		return {'message': 'restaurant not found'}, 404

	def post(self, name):
		if RestaurantModel.find_by_name(name):
			return {'message': "A restaurant with name '{}' already exists.".format(name)}, 400

		restaurant = RestaurantModel(name)
		try:
			restaurant.save_to_db()
		except:
			return {'message': 'An error occurred while creating the restaurant'}, 500

		return restaurant.json(), 201

	def delete(self, name):
		restaurant = RestaurantModel.find_by_name(name)
		if restaurant:
			restaurant.delete_from_db()

		return {'message': 'restaurant deleted'}
