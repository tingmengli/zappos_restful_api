import sqlite3
from db import db 

class MenuModel(db.Model):
	__tablename__ = 'menus'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80))

	items = db.relationship('ItemModel', lazy='dynamic') # many items relate to one menu
	restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'))
	restaurant = db.relationship('RestaurantModel') # one menu belongs to only one restaurant

	def __init__(self, name, restaurant_id):
		self.name = name
		self.restaurant_id = restaurant_id

	def json(self):
		return {'menu id': self.id, 'name': self.name, 'items': [item.json() for item in self.items.all()]}

	@classmethod
	def find_by_id(cls, _id):
		return cls.query.filter_by(id=_id).first() # SELECT * FROM items WHERE name=name LIMIT 1

	def save_to_db(self):
		db.session.add(self)
		db.session.commit()

	def delete_from_db(self):
		db.session.delete(self)
		db.session.commit()
