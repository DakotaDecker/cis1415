class ItemToPurchase:

    def __init__(self,  item_description='none', item_name=0, item_price=0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def __str__(self):
        return ('%s %d @ $%d = $%d' %
                (self.item_name, self.item_quantity, self.item_price, (self.item_quantity * self.item_price)))


if __name__ == "__main__":
    item1 = ItemToPurchase()
    item1.item_name = input('Item 1\nEnter the item name:\n')
    item1.item_price = int(input('Enter the item price:\n'))
    item1.item_quantity = int(input('Enter the item quantity:\n'))
    item2 = ItemToPurchase()
    item2.item_name = input('\nItem 2\nEnter the item name:\n')
    item2.item_price = int(input('Enter the item price:\n'))
    item2.item_quantity = int(input('Enter the item quantity:\n'))

    print('\nTOTAL COST')
    print(item1)
    print(item2)
    print('\nTotal: $%d' % ((item1.item_quantity * item1.item_price) + (item2.item_quantity * item2.item_price)))

