from item import Item
from errors import ItemNotExistError
from errors import ItemAlreadyExistsError


class ShoppingCart:
    def __init__(self):
        self.items = []  # Contains the items of the cart 

    def add_item(self, item: Item):
        '''adding item to the cart'''
        if item in self.items:
            raise ItemAlreadyExistsError("The item already exists")
        self.items.append(item)

    def remove_item(self, item_name: str):
        '''removing item from the cart'''
        for item in self.items:
            if item.name in item_name:
                self.items.remove(item)
                return
        raise ItemNotExistError("No item with the given name exists")

    def get_subtotal(self) -> int:
        '''get the price for all the items'''
        return sum(item.price for item in self.items)
