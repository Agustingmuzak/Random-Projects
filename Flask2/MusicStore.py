
### We define a general product for our store, this product must have a cost and a price, the difference between the cost and the price is the profit
class Product:
    def __init__(self, cost, price):
        self.cost = cost
        self.price = price
    def getProfit(self):
        profit = (self.price - self.cost)
        return 'The profit is {}'.format(profit)
    def getCost(self):
        return self.cost
    def getPrice(self):
        return self.price
        
### Instrument is a type of Product, the instrument will have an instrument_type (a.k.a: Guitar, Drums, Saxophone, etc) and a sub_category (a.k.a: Electric, Acoustic, Tenor, etc)
class Instrument:
    def __init__(self, instrument_type, sub_category):
        self.instrument_type = instrument_type
        self.sub_category = sub_category
    def getDetail(self):
        return 'The instrument is: {} {}'.format(self.sub_category, self.instrument_type)
    
### Guitar is a type of instrument, it inherits all methods from Product and Instrument, a guitar will have a brand (a.k.a: Gibson, Fender, etc) and model (a.k.a: Les Paul, Stratocaster, etc)        
class Guitar(Instrument, Product):
    def __init__(self, instrument_type, sub_category, brand, model, cost, price):
        Instrument.__init__(self, instrument_type, sub_category) 
        Product.__init__(self, cost, price)
        self.brand = brand
        self.model = model
    def guitarDetail(self):
        return 'This instrument is a {} {} {} {}'.format(self.brand, self.model, self.sub_category, self.instrument_type)
    def getName(self):
        return '{} {} {} {}'.format(self.brand, self.model, self.sub_category, self.instrument_type)
            

### A shopping cart object will store all the items selected for purchase, we will store an item price and quantity of items purchased   


guitar1 = Guitar('Guitar', 'Electric', 'Gibson', 'Les Paul Standard', 1100, 2300)
guitar2 = Guitar('Guitar', 'Electric', 'Fender', 'American Standard', 1300, 2000)
bassguitar1 = Guitar('Bass', 'Electric', 'Fender', 'Precision', 1500, 2100 )

my_shopping_dict = {
    guitar1 : 2, 
    guitar2 : 1,
    bassguitar1 : 1
}


class ShoppingCart(Guitar):
    def __init__(self, items_cost, quantity, items_name):
        self.items_cost = items_cost
        self.quantity = quantity
        self.items_name = items_name

    def getNamesList(self):
        names_list = []
        for i in self.items_name:
            names_list.append(i.getName())
        return names_list
    
    def getPriceList(self):
        prices_list = []
        for i in self.items_cost:
            prices_list.append(i.getPrice())
        return prices_list
    
    def getQtyList(self):
        qty_list = []
        for i in self.quantity:
            qty_list.append(i)
        return qty_list
    def getTotal(self):
        total_list1 = []
        total_prices = shopping_cart.getPriceList()
        total_names = shopping_cart.getNamesList()
        total_qty = shopping_cart.getQtyList()

        for n in range(0, len(total_prices)):
            total_list1.append(total_prices[n] * total_qty[n])
        total_num = sum(total_list1)
        
        return total_prices, total_names, total_qty, total_num

shopping_cart = ShoppingCart(list(my_shopping_dict.keys()), list(my_shopping_dict.values()), list(my_shopping_dict.keys()))

print(shopping_cart.getTotal())   





    


