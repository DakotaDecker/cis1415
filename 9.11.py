class ItemToPurchase:

    def __init__(self, item_name=0, item_price=0, item_quantity=0, item_description='none'):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def __str__(self):
        return ('%s %d @ $%d = $%d' %
                (self.item_name, self.item_quantity, self.item_price, (self.item_quantity * self.item_price)))

    def print_item_description(self):
        print('%s: %s' % (self.item_name, self.item_description))

    
class ShoppingCart:
    def __init__(self, customer_name='none', current_date='January 1, 2016'):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, items):
        self.cart_items.append(items)

    def remove_item(self, item_name):
        if item_name in cart_items:
            cart_items.remove(item_name)
        else:
            print('Item not found in cart. Nothing removed.')
            

if __name__ == "__main__":
    item1 = ItemToPurchase()
    item1.item_name = input('Item 1\nEnter the item name:\n')
    item1.item_price = int(input('Enter the item price:\n'))
    item1.item_quantity = int(input('Enter the item quantity:\n'))
    item2 = ItemToPurchase()
    item2.item_name = input('\nItem 2\nEnter the item name:\n')
    item2.item_price = int(input('Enter the item price:\n'))
    item2.item_quantity = int(input('Enter the item quantity:\n'))
    cart = ShoppingCart()

    print('\nTOTAL COST')
    print(item1)
    print(item2)
    print('\nTotal: $%d' % ((item1.item_quantity * item1.item_price) + (item2.item_quantity * item2.item_price)))
    cart.add_item(item1)
    cart.add_item(item2)

