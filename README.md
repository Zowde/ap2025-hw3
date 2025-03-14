The following files were provided as part of the course and were not written by me:
- All **test files** (located in the `src/test` or `tests` directory).
- The **Gradle build files** (such as `build.gradle` or `settings.gradle`).

I wrote the rest of the code myself.


**Background**
In recent years, many people choose to do their shopping online. Seeing this great business opportunity, you decide to open up your own online store for the masses. In this store you’ll be able to offer all sorts of items, give out special deals to your customers and most importantly, charge for the products you sell.

Being a gifted Python programmer you decide to write the main logic of the online store in Python. You will write an API for the front end to use when it is eventually implemented.



**Design**
After an extensive brainstorming session you have reached the following design:

Each item in your store will be an instance of the class Item (this class is further described below).

When first initailizing the store, it would load a file with all the available items.

Customers will be able to do the following:

Search for items
Add items to their shopping cart
Remove items from their shopping cart
Purchase the items in their shopping cart
For extra profit, similar items to the ones the customer purchased will be highlighted.

It may sound like a lot, but one step (i.e., one line) at a time leads to the finish line!



Item Class
Items are made up of the following fields:

Name
Price
Hashtags – A list of words tagging the item.
Description
A __str__() function has been provided to you.

Assumptions

You may assume each name is associated with at most one item.
The hashtags list may be empty.
The hashtags list does not contain duplicates.


ShoppingCart Class
A skeleton of the class is provided to you with the following methods for you to implement:

add_item(self, item)

Adds the given item to the shopping cart.
Arguments: the current instance of ShoppingCart and an instance of Item.
Exceptions: if the item name already exists in the shopping cart, raises ItemAlreadyExistsError.
remove_item(self, item_name)

Removes the item with the given name from the shopping cart
Aguments: the current instance of ShoppingCart and an instance of str.
Exceptions: if no item with the given name exists, raises ItemNotExistError.
get_subtotal(self) – Returns the subtotal price of all the items currently in the shopping cart.



Store Class
A skeleton of the class is provided to you. The class has a single constructor which takes a path to an items file and loads it into the items field of the class. Do not alter this code!

The Store class has the following methods for you to implement:

search_by_name(self, item_name)

Arguments: the current instance of Store and an instance of str.
Return value: a sorted list of all the items that match the search term. The sort order is described below.
The items in the returned list must contain the given phrase (and do not have to exactly match it). For example, when searching for "soap", items such as "dish soap" and "body soap" should be returned.
search_by_hashtag(self, hashtag)

Arguments: the current instance of Store and an instance of str.
Return value: a sorted list of all the items matching the search criterion. The sort order is described below.
The items in the returned list must have the given hashtag in their hashtag list. For example, when searching for the hashtag "paper", items with hashtags such as "tissue paper" must not be returned.
add_item(self, item_name)

Adds an item with the given name to the customer’s shopping cart.
Arguments: the current instance of Store and an instance of str.
Exceptions: if no such item exists, raises ItemNotExistError. If there are multiple items matching the given name, raises TooManyMatchesError. If the given item is already in the shopping cart, raises ItemAlreadyExistsError.
To ease the search for the customers, not the whole item’s name must be given, but rather a distinct substring. For example, when adding "soap" to the cart, if an item such as "body soap" exists, and no other item with the substring "soap" in its name, "body soap" should be added to the list.
You may assume that no two items exist such that one's name is a substring of the other.
remove_item(self, item_name)

Removes an item with the given name from the customer’s shopping cart.
Arguments: the current instance of Store and an instance of str.
Exceptions: if no such item exists, raises ItemNotExistError. If there are multiple items matching the given name, raises TooManyMatchesError.
In a similar fashion to add_item, here too, not the whole item’s name must be given for it to be removed.
checkout(self) – Returns the total price of all the items in the costumer’s shopping cart.

Search results:

For both search functions, the list returned must not include items which are already in the current shopping cart. The result list should be ordered as follows.

Let the list of all items in the current shopping cart be Items, and let the list of all hashtags of Items be Tags (note that Tags may have duplicates).

An item i1 would be before item i2 in the result list if i1 has more common hashtags with Tags than i2.

If both i1 and i2 have the same number of common hashtags with Tags, than i1 would appear before i2 if i1.name appears before i2.name in the lexicographic order.
