#python3

#Print the initial inventory of the bike shop for each bike it carries.

#After each customer has purchased their bike, the script should print out the#
#bicycle shop's remaining inventory for each bike, and how much profit they
#have made selling the three bikes


class Bicycle(object):
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
            bike.stock = 1
        self.profits = 0
        
    def sell(self, bike):
        self.profits += bike.salesprice
        bike.stock -= 1 
        
    def print_status(self):
        for bike in self.inventory:
            pass #TODO inventory + self.profit

    #func to buy more bikes
            

class Customer(object):
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
        print("From '{}' {} can afford: {}".format(shop, self.name, self.affordable))
        
        
    def buy(self, bike, shop):
        """ Takes bike object and shop as arguments. 
        Appends bought bike to customers bike list, deducts  salesprice in shop 
        from budget and calls sell method from shop instance."""
        
        self.bikes.append(bike.model)
        self.budget -= bike.salesprice
        print("{} just bought a {} for $ {} and now has $ {} left".format(self.name, bike.model, int(bike.salesprice), int(self.budget)))
        shop.sell(bike)



## TESTING
bike1 = Bicycle("Mountain Bike", 6, 500)
bike2 = Bicycle("Unisex", 7.5, 600)
bike3 = Bicycle("Racer", 5, 800)
bike4 = Bicycle("Children's tricycle", 4, 400)
bike5 = Bicycle("Electric rider", 10, 900)
bike6 = Bicycle("Boring bike", 8, 150)

customer1 = Customer("Claudia", 200)
customer2 = Customer("Julia", 500)
customer3 = Customer("Nana", 1000)

citybikes_stock = [bike1, bike2, bike3, bike4, bike5, bike6]
citybikes = Bike_shop("City Bikes", citybikes_stock, 15)
customer1.buy(bike6, citybikes)
customer2.buy(bike4, citybikes)
customer3.buy(bike3,citybikes)
