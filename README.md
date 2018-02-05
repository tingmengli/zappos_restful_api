# Restaurant_api  
* A restaurant menu api based on Flask using SQLAlchemy  

* Has a list of restaurants. You can add/delete/edit a restaurant.  
* Restaurant has: restaurant_id, name.  
* Each restaurant has one or many menus. You can add/delete/edit which menu the restaurant has.  
* Menu has: menu_id, name, restaurant_id. 
* Each menu has one or many items. You can add/delete/edit which item the menu has.  
* Item on the menu has: item_id, name, price, menu_id. 
 

## Restaurant End-points:
* `/restaurants/`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; GET method to show all restaurants.
* `/restaurant/new/`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; POST method to add a new restaurant.
* `/restaurant/<restaurantid>`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; GET, PUT and DELETE a restaurant.


## Menu End-points:
* `/menu/<menuid>`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; GET, PUT and DELETE a menu.  
* `/menu/new/`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; POST a new menu.


## Item End-points:
* `/item/<itemid>`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; GET, PUT and DELETE an item.  
* `/item/new/`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; POST a new item.