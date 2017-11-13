class CellPhone:
    def __init__(self):
        self.manufact = ''
        self.model = ''
        self.retail_price = 0

    def set_manufact(self, manufact):
        self.manufact = manufact

    def set_model(self, model):
        self.model = model

    def set_retail_price(self, retail_price):
        self.retail_price = retail_price

    def get_manufact(self):
        print('Manufacturer:', self.manufact)

    def get_model(self):
        print('Model Number:', self.model)

    def get_retail_price(self):
        print('Retail Price: $%.2f' % self.retail_price)


phone = CellPhone()
phone.manufact = input('Enter the manufacturer: ')
phone.model = input('Enter the model number: ')
phone.retail_price = float(input('Enter the retail price: '))
print('Here is the data that you entered: ')
phone.get_manufact()
phone.get_model()
phone.get_retail_price()
