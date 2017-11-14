class CellPhone:
    def __init__(self):
        self.manufact = 'none'
        self.model = 0
        self.retail_price = 0
    def get_manufact(self):
        print('Manufacturer:', item.manufact)
    def get_model(self):
        print('Model Number:', item.model)
    def get_retail_price(self):
        print('%s%.2f' % ('$', item.retail_price))

set_manufact = str(input())
set_model = input()
set_retail_price = float(input())

item = CellPhone()
item.manufact = set_manufact
item.model = set_model
item.retail_price = set_retail_price

if __name__ == "__main__":
    print('Enter the manufacturer:')
    print('Enter the model number:')
    print('Enter the retail price:')
    print('Here is the data that you entered:')
    item.get_manufact(),
    item.get_model(),
    item.get_retail_price(),
    
    
