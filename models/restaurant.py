import sqlite3
from db import db 

class RestaurantModel(db.Model):
	__tablename__ = 'restaurants'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80))

	menus = db.relationship('MenuModel', lazy='dynamic') # many items relate to one menu

	def __init__(self, name):
		self.name = name

	def json(self):
		return {'restaurant id': self.id, 'name': self.name, 'menus': [menu.json() for menu in self.menus.all()]}

	@classmethod
	def find_by_id(cls, _id):
		return cls.query.filter_by(id=_id).first() # SELECT * FROM items WHERE name=name LIMIT 1

	def save_to_db(self):
		db.session.add(self)
		db.session.commit()

	def delete_from_db(self):
		db.session.delete(self)
		db.session.commit()

