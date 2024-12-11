#from store import Store
from item import Item  # Imports the Item class from the item.py file
from shopping_cart import ShoppingCart  # Imports the ShoppingCart class from shopping_cart.py
'''
POSSIBLE_ACTIONS = [
    'search_by_name',
    'search_by_hashtag',
    'add_item',
    'remove_item',
    'checkout',
    'exit'
]

ITEMS_FILE = 'items.yml'


def read_input():
    line = input('What would you like to do?')
    args = line.split(' ')
    return args[0], ' '.join(args[1:])
'''

def main():
  '''
    store = Store(ITEMS_FILE)
    action, params = read_input()
    while action != 'exit':
        if action not in POSSIBLE_ACTIONS:
            print('No such action...')
            continue
        if action == 'checkout':
            print(f'The total of the purchase is {store.checkout()}.')
            print('Thank you for shopping with us!')
            return
        if action == 'exit':
            print('Goodbye!')
            return
        getattr(store, action)(params)
    
        action, params = read_input()

'''
 # Create an instance of the Item class
item1 = Item("Wireless Mouse", 29.99, "A smooth wireless mouse with ergonomic design.", ["electronics", "mouse", "wireless"])
y = ShoppingCart()
y.add_item(item1)
word = item1.getitemname()
y.remove_item(word)


if __name__ == '__main__':
    main()
