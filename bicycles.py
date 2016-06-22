#python3


class Bicycle(object):
    """Base class for bicycles"""
    def __init__(self, model, kilos, cost, brand="Generic"):
        self.model = model
        self.weight = kilos
        self.cost = cost
        self.brand = brand


class Manufacturer(object):
    """ Has a name (string) and a profit margin (number). 
        Can make_bikes, returned in list object"""
    def __init__(self, name, margin):
        self.name = name
        self.margin = margin
        
    def make_bikes(self, model, kilo, cost_per_bike, number_of_bikes):
        bikes_produced = []
        for i in range(number_of_bikes):
            bikes_produced.append(Bicycle(model, kilo, cost_per_bike, brand=self.name))
        
class Sportsbikes(Manufacturer):
    pass
    #super for init and make_bikes, filled out variables, depending on type

class Citybikes(Manufacturer):
    pass 
    #super for init and make_bikes, filled out variables, depending on type


class Bike_shop(object):
    """Bike_shop takes 3 arguments: name (string), inventory (list of Bicycle instances) and margin (as percent)"""
    def __init__(self, name, inventory, margin=20):
        self.name = name
        self.inventory = inventory.copy() #makes shallow copy to not affect orig. bikes
        #should start with empty stock and working capital
        for bike in self.inventory:
            bike.salesprice = bike.cost * (1 + margin/100)
            bike.profit = bike.salesprice - bike.cost
            bike.stock = 1 #should refer to number from bought bikes 
        self.profits = 0
        #TODO Would it be better to use dict to keep track of model and stock?
        # And what would __init__ and a buy method have to look like?


    def sell(self, bike):
        self.profits += bike.profit
        bike.stock -= 1 

        
    def print_status(self):
        print("Inventory status:")
        for bike in self.inventory:
            print("Model: {} - in stock: {}".format(bike.model, bike.stock))
        print("Total profits: ${}".format(round(self.profits,2)))
        print()

    #TODO func to buy more bikes (order from manufacturer, get list object and merge to stock)
    


class Customer(object):
    """Base class for customers. Can own and buy bicycles"""
    def __init__(self, name, budget, bikes = []):
        self.name = name
        self.budget = budget
        self.bikes = bikes
        
        
    def can_afford(self, shop):
        """Prints the name of customer, and a list of bikes in a given 
        bike shop that the customer can afford with their budget. """
        self.affordable = []
        for bike in shop.stock:
            if bike.salesprice <= self.budget:
                self.affordable.append(bike.model)
        #TODO print function should return affordable as comma separated strings
        print("From '{}' {} can afford: {}.".format(shop, self.name, self.affordable))
        
        
    def buy(self, bike, shop):
        """ Takes bike object and shop as arguments. 
        Appends bought bike to customers bike list, deducts  salesprice in shop 
        from budget and calls sell method from shop instance."""
        
        self.bikes.append(bike.model)
        self.budget -= bike.salesprice
        print("{} just bought a {} for ${} and now has ${} left.".format(self.name, bike.model, int(bike.salesprice), int(self.budget)))
        print()
        shop.sell(bike)

