# Restaurant_api
 A restaurant menu api based on Flask using SQLAlchemy

 Has a list of restaurants. You can add/delete/edit a restaurant.
 Restaurant has: restaurant_id, name, primary key is restaurant_id.
 Each restaurant has one or many menus. You can add/delete/edit which menu the restaurant has.
 Menu has: menu_id, name, restaurant_id. primary key is menu_id, foreign key is restaurant_id.
 Each menu has one or many items. You can add/delete/edit which item the menu has.
 Item on the menu has: item_id, name, price, menu_id. Primary key is item_id, foreign key is menu_id.

 Restaurant End-points:
 / or /restaurants/			Show all restaurants.
 /restaurant/new/			Add a new restaurant.
 /restaurant/<id>/edit		Edit a restaurant.
 /restaurant/<id>/delete/	Delete a restaurant

 Menu End-points:
 /restaurant/<id>/			Show the full menu.
 /restaurant/<id>/new/		Add a new menu
 /restaurant/<id>/<menuid>/edit 	Edit a menu
 /restaurant/<id>/<menuid>/delete   Delete a menu

 Item End-points:
 /restaurant/<id>/<menuid>/<itemid>		Show the item and price
 /restaurant/<id>/<menuid>/new	 		Add a new item
 /restaurant/<id>/<menuid>/<itemid>/edit  Edit an item
 /restaurant/<id>/<menuid>/<itemid>/delete Delete an item
