class ToPurchase:
    def __init__(self, item_name=0, item_price=0, item_quantity=0, item_description='none'):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        self.item_description = item_description

    def print_item_cost(self):
        print(items1.item_name, items1.item_quantity, '@ %s%.0f' % ('$', items1.item_price), '= %s%.0f' % ('$', items1.added_total()))
        print(items2.item_name, items2.item_quantity, '@ %s%.0f' % ('$', items2.item_price), '= %s%.0f' % ('$', items2.added_total()))
        print(items3.item_name, items3.item_quantity, '@ %s%.0f' % ('$', items3.item_price), '= %s%.0f' % ('$', items3.added_total()))

    def added_total(self):
        return self.item_quantity * self.item_price

    def sum_total(self):
        return items1.added_total() + items2.added_total() + items3.added_total()
            
    def print_item_description(self):
        print('%s%s' % (items1.item_name, ':'), items1.item_description)
        print('%s%s' % (items2.item_name, ':'), items2.item_description)
        print('%s%s' % (items3.item_name, ':'), items3.item_description)

class ShoppingCart:
    def __init__(self, customer_name='none', current_date='January 1, 2016'):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []
        
    def add_items(self, items):
        self.cart_items.append(items)
        
input_name = str(input())
input_price = float(input())
input_description = input()
input_quantity = int(input())

input2_name = str(input())
input2_price = float(input())
input2_description = input()
input2_quantity = int(input())

input3_name = input()
input3_price = float(input())
input3_description = input()
input3_quantity = int(input())

user_name = str(input())
user_date = input()

items1 = ToPurchase()
items1.item_name = input_name
items1.item_price = input_price
items1.item_description = input_description
items1.item_quantity = input_quantity

items2 = ToPurchase()
items2.item_name = input2_name
items2.item_price = input2_price
items2.item_description = input2_description
items2.item_quantity = input2_quantity

items3 = ToPurchase()
items3.item_name = input3_name
items3.item_price = input3_price
items3.item_description = input3_description
items3.item_quantity = input3_quantity

cart_items = ShoppingCart()
cart_items.customer_name = user_name
cart_items.current_date = user_date

if __name__ == "__main__":
    print(cart_items.customer_name, 'Shopping Cart -', cart_items.current_date, '\n')
    
    items1.print_item_cost(),
    print('\nTotal:', '%s%.0f' % ('$', items1.sum_total()), '\n')
    print('Item Descriptions')
    items1.print_item_description(),
