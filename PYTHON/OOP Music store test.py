class Guitar:
    guitar_list = []
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        Guitar.guitar_list.append("{}, {}".format(self.brand, self.model))

        
        

guitar1 = Guitar('Gibson', 'Les Paul')
guitar2 = Guitar('Fender', 'Stratocaster')
guitar3 = Guitar('PRS', 'Custom')

print(Guitar.guitar_list)


    