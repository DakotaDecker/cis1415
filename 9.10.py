class ItemToPurchase:

    def __init__(self,  item_description='none', item_name=0, item_price=0, item_quantity=0):
        # Initializes a new item
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def __str__(self):
        # Changes the print statement to print a line with the name of the item, how many are in the cart,
        # the cost of a single item, and the cost for how many are in your cart
        return ('%s %d @ $%d = $%d' %
                (self.item_name, self.item_quantity, self.item_price, (self.item_quantity * self.item_price)))


if __name__ == "__main__":
    item1 = ItemToPurchase()  # Creates a new item "item1" with default values
    item1.item_name = input('Item 1\nEnter the item name:\n')  # Prompts user to enter the name of the new item
    item1.item_price = int(input('Enter the item price:\n'))  # Prompts user to enter the price of one unit of the new item
    item1.item_quantity = int(input('Enter the item quantity:\n'))  # Prompts the user to enter how many of that item to add to their cart
    item2 = ItemToPurchase()  # Creates a new item "item2" with default values
    item2.item_name = input('\nItem 2\nEnter the item name:\n')  # Prompts user to enter the name of the new item
    item2.item_price = int(input('Enter the item price:\n'))  # Prompts user to enter the price of one unit of the new item
    item2.item_quantity = int(input('Enter the item quantity:\n'))  # Prompts the user to enter how many of that item to add to their cart

    print('\nTOTAL COST')
    print(item1)  # Prints the values associated with the item using the custom print method 
    print(item2)  # Prints the values associated with the item using the custom print method 
    # Calculates and prints the total cost of all the items in the cart
    print('\nTotal: $%d' % ((item1.item_quantity * item1.item_price) + (item2.item_quantity * item2.item_price)))

