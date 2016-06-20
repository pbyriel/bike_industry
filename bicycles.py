#python3


class Bicycle(object):
    """Base class for bicycles"""
    def __init__(self, model, kilos, cost, brand="Generic brand"):
        self.model = model
        self.weight = kilos
        self.cost = cost
        self.brand = brand


class Bike_shop(object):
    """Bike_shop takes 3 arguments: name (string), inventory (list of Bicycle instances) and margin (as percent)"""
    def __init__(self, name, inventory, margin=20):
        self.name = name
        self.inventory = inventory.copy() #makes shallow copy to not affect orig. bikes
        for bike in self.inventory:
            bike.salesprice = bike.cost * (1 + margin/100)
            bike.profit = bike.salesprice - bike.cost
            bike.stock = 1
        self.profits = 0
        
    def sell(self, bike):
        self.profits += bike.profit
        bike.stock -= 1 
        
    def print_status(self):
        print("Inventory status:")
        for bike in self.inventory:
            print("Model: {} - in stock: {}".format(bike.model, bike.stock))
        print("Total profits: ${}".format(int(self.profits)))
        print()

    #TODO func to buy more bikes
            

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

