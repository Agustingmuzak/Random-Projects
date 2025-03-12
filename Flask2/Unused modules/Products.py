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
    
