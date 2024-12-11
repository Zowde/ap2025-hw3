from item import Item

class ItemNotExistError(Exception):
    pass

class ItemAlreadyExistError(Exception):
    pass


class ShoppingCart:
    def __init__(self):
        self.items = []  # Contains the items of the cart 

    def add_item(self, item: Item):
        if item in self.items:
            raise ItemAlreadyExistError("The item already exists")
        self.items.append(item)

    def remove_item(self, item_name: str):
        for item in self.items:
            if item.name == item_name:
                self.items.remove(item)
                return
        raise ItemNotExistError("No item with the given name exists")

    def get_subtotal(self) -> int:
        return sum(item.price for item in self.items)
