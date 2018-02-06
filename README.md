# Restaurant_api  
* A restaurant menu api based on Flask using SQLAlchemy and Flask JWT

* Has a list of restaurants. You can add/delete/edit a restaurant.  
* Restaurant has: restaurant_id, name.  
* Each restaurant has one or many menus. You can add/delete/edit which menu the restaurant has.  
* Menu has: menu_id, name, restaurant_id. 
* Each menu has one or many items. You can add/delete/edit which item the menu has.  
* Item on the menu has: item_id, name, price, menu_id.
* GET methods require JWT token for user authentication.  
 

## Restaurant End-points:
* `/restaurants/`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; GET method to show all restaurants, menus of each restaurant and items of each menu.
* `/restaurant/new/`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; POST method to add a new restaurant.
* `/restaurant/<restaurantid>`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; GET, PUT and DELETE a restaurant.


## Menu End-points:
* `/menu/<menuid>`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; GET, PUT and DELETE a menu.  
* `/menu/new/`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; POST a new menu.


## Item End-points:
* `/item/<itemid>`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; GET, PUT and DELETE an item.  
* `/item/new/`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; POST a new item.

## User register End-points:
* `/register`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Register a new user with username and password
* `/auth`&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Authentication with username and password, generates an access_token.

## API testing:
* Import zappos_oa.postman_collection.json file into Postman and use the endpoints for sending and retrieving information.