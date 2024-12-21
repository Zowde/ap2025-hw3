import yaml
import pytest
from item import Item
from shopping_cart import ShoppingCart
from errors import ItemNotExistError, ItemAlreadyExistsError, TooManyMatchesError

class Store:
    def __init__(self, path):
        with open(path) as inventory:
            items_raw = yaml.load(inventory, Loader=yaml.FullLoader)['items']
        self._items = self._convert_to_item_objects(items_raw)
        self._shopping_cart = ShoppingCart()

    @staticmethod
    def _convert_to_item_objects(items_raw):
        return [Item(item['name'],
                     int(item['price']),
                     item['hashtags'],
                     item['description'])
                for item in items_raw]

    def get_items(self) -> list:
        return self._items

    def search_by_name(self, item_name: str) -> list:
      '''Filter items whose name contains the search term (case-insensitive) and not inside SC'''
      matching_items=[]
      for item in self._items:
          if item_name in item.name and item not in self._shopping_cart.items:
             
             matching_items.append(item)
    
     
    # Get hashtags from all the itemse inside the SC (case-insensitive)
      cart_hashtags = [hashtag for item in self._shopping_cart.items for hashtag in item.hashtags]
    # we should sort the mathcing_items according the cart_hashtags
      matching = sorted(matching_items,key=lambda item:item.name)
      result_items = sorted (matching,key=lambda item: self.count_common_hashtags_for_item(item.hashtags,cart_hashtags),reverse=True)
    
      return result_items
    def count_common_hashtags_for_item(self,list1,list2):
        '''list hashtags , list2 tags'''
        count = 0
        for ht in list1:
            for htag in list2:
                if htag == ht:
                    count += 1
        return count   
    

    def search_by_hashtag(self, hashtag: str) -> list:
               
                ''' Filter items whose hashtags contain the search term (case-insensitive)'''
                matching_items = [item for item in self._items 
                      if hashtag.lower() in (h.lower() for h in item.hashtags) and item not in self._shopping_cart.items]
    
    # Get hashtags from the items in the shopping cart once (case-insensitive)
                cart_hashtags = [hashtag.lower() for item in self._shopping_cart.items for hashtag in item.hashtags]
    
    # Sort the items first by the number of common hashtags with the cart, then by name (case-insensitive)
                matching_items.sort(key=lambda item: (
                -sum(hashtag in cart_hashtags for hashtag in item.hashtags),  # Number of common hashtags
                item.name.lower()  # Lexicographical order (case-insensitive)
    ))

                return matching_items

 
    def add_item(self, item_name: str):
       '''Search for items that match the given name (substring)'''
       matching_items = [item for item in self._items if item_name in item.name]
    
       if len(matching_items) == 0:
           raise ItemNotExistError("No such item exists")
       elif len(matching_items) > 1:
           raise TooManyMatchesError("Multiple items match the given name")
    
       item = matching_items[0]
    
    # Add the item to the shopping cart
       self._shopping_cart.add_item(item)

    def remove_item(self, item_name: str):
        ''' Search for items that match the given name (substring)'''
        matching_items = [item for item in self._items if item_name.lower() in item.name.lower()]
        
        if len(matching_items) == 0:
            raise ItemNotExistError("No such item exists")
        elif len(matching_items) > 1:
            raise TooManyMatchesError("Multiple items match the given name")
        
        item = matching_items[0]
        
        # Remove the item from the shopping cart
        self._shopping_cart.remove_item(item.name)

    def checkout(self) -> int:
        # Return the total price of items in the shopping cart
        return self._shopping_cart.get_subtotal()
