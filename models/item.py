import sqlite3
from db import db 

class ItemModel(db.Model):
	__tablename__ = 'items'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80))
	price = db.Column(db.Float(precision=2))

	menu_id = db.Column(db.Integer, db.ForeignKey('menus.id'))
	menu = db.relationship('MenuModel') # one item belongs to only one menu

	def __init__(self, name, price, menu_id):
		self.name = name
		self.price = price
		self.menu_id = menu_id

	def json(self):
		return {'item id': self.id, 'name': self.name, 'price': self.price}

	@classmethod
	def find_by_id(cls, _id):
		return cls.query.filter_by(id=_id).first() # SELECT * FROM items WHERE name=name LIMIT 1

	def save_to_db(self):
		db.session.add(self)
		db.session.commit()

	def delete_from_db(self):
		db.session.delete(self)
		db.session.commit()
