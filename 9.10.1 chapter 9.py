class ToPurchase:
    def __init__(self):
        self.item_name = 'none'
        self.item_price = 0
        self.item_quantity = 0
        
    def print_item_cost(self):
        print(items1.item_name, items1.item_quantity, '@ %s%.0f' % ('$', items1.item_price), '= %s%.0f' % ('$', items1.added_total()))
        print(items2.item_name, items2.item_quantity, '@ %s%.0f' % ('$', items2.item_price), '= %s%.0f' % ('$', items2.added_total()))
        
    def added_total(self):
        return self.item_quantity * self.item_price
        
    def sum_total(self):
        return items1.added_total() + items2.added_total()
        
    def total_sum(self):
        print('%s%.0f' % ('$', items1.sum_total()))
input_name = str(input())
input_price = float(input())
input_quantity = int(input())

input_N = str(input())
input_P = float(input())
input_Q = int(input())

items1 = ToPurchase()
items1.item_name = input_name
items1.item_quantity = input_quantity
items1.item_price = input_price

items2 = ToPurchase()
items2.item_name = input_N
items2.item_quantity = input_Q
items2.item_price = input_P

if __name__ == "__main__":
    print('Item 1')
    print('Enter the item name:')
    print('Enter the item price:')
    print('Enter the item quantity:\n')
    
    print('Item 2')
    print('Enter the item name:')
    print('Enter the item price:')
    print('Enter the item quantity:\n')
    
    print('TOTAL COST')
    items1.print_item_cost(),
    
    print('\nTotal:', '%s%.0f' % ('$', items1.sum_total()))
