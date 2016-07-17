#python3


class Bicycle(object):
    """Base class for bicycles"""
    def __init__(self, model, kilos, cost, brand="Generic"):
        self.model = model
        self.weight = kilos
        self.cost = cost
        self.brand = brand



class Manufacturer(object):
    """ Has a name (string), profit margin (number) and a type (string). 
        Can make_bikes, returned in list object"""
    def __init__(self, name, margin, type):
        self.name = name
        self.margin = margin
        self.type = type


    def make_bike(self, model, kilos, cost):
        bike = Bicycle(model, kilos, cost=cost*(1 + self.margin/100), brand=self.name)
        print(bike.cost)
        return bike



class Sportsbikes(Manufacturer):
    def __init__(self):
        super(Sportsbikes, self).__init__(name="Sporty", margin=35, type="Sports bikes manufacturer")
        # MENTOR: I don't understand why I have to provide arguments to super
    
    
    def make_mountain_bike(self):
       return super(Sportsbikes, self).make_bike(model="Mountain bike", kilos=6, cost=200)
    
    
    def make_racing_bike(self):
        return super(Sportsbikes, self).make_bike(model="Racing bike", kilos=5, cost=300)


    def make_pro_bike(self):
       return super(Sportsbikes, self).make_bike(model="Pro bike", kilos=4.5, cost=400)



class Citybikes(Manufacturer):
    def __init__(self):
        super(Citybikes, self).__init__(name=None, margin=30, type="City bikes manufacturer")


    def make_urban_bike(self):
        return super(Citybikes, self).make_bike(model="Urban", kilos=6, cost=250)
    
    
    def make_child_bike(self):
        return super(Citybikes, self).make_bike(model="Children's tricycle", kilos=4, cost=200)   


    def make_electric_bike(self):
        return super(Citybikes, self).make_bike(model="Electric rider", kilos=9, cost=800)



class Bike_shop(object):
    """Bike_shop takes 4 arguments: name (string), inventory (list of Bicycle instances) and margin (as percent)"""
    def __init__(self, name, inventory=[], capital=5000, margin=20, profits=0):
        self.name = name
        self.inventory = inventory
        self.capital = capital
        self.margin = margin
        self.profits = profits
        #TODO Would it be better to use dict to keep track of model and stock?
        # And what would __init__ and a buy method have to look like?


    def print_status(self):
        print("Inventory status:")
        for bike in self.inventory:
            print("Model: {} - in stock: {}".format(bike.model, bike.stock))
        print("Total profits: ${}".format(round(self.profits,2)))
        print("Working capital: ${}".format(round(self.capital,2)))
        print()


    def buy(self, bikes):
        print(bikes)
        for bike in bikes:
            bike.salesprice = bike.cost * (1 + self.margin/100)
            bike.profit = bike.salesprice - bike.cost
            bike.stock = 1 
            self.inventory.append(bike)
            self.capital -= bike.cost
            

    def sell(self, bike):
        self.profits += bike.profit
        self.capital += bike.salesprice
        bike.stock -= 1 
        #TODO stock is actually wrong if bike bought before
   


class Customer(object):
    """Base class for customers. Can own and buy bicycles"""
    def __init__(self, name, budget, bikes = []):
        self.name = name
        self.budget = budget
        self.bikes = bikes
    
        
    def can_afford(self, shop):
        """Prints the name of customer, and a stringed list of bikes in a given 
        bike shop that the customer can afford with their budget. """
        self.affordable = ""
        for bike in shop.stock:
            if bike.salesprice <= self.budget:
                self.affordable += (bike.model + ", ")
        payable = "From '{}' {} can afford: {}.".format(shop, self.name, self.affordable)
        print(payable.rstrip(", "))
    
        
    def buy(self, bike, shop):
        """ Takes bike object and shop as arguments. 
        Appends bought bike to customers bike list, deducts  salesprice in shop 
        from budget and calls sell method from shop instance."""
        self.bikes.append(bike.model)
        self.budget -= bike.salesprice
        print("{} just bought a {} for ${} and now has ${} left.".format(self.name, bike.model, int(bike.salesprice), int(self.budget)))
        print()
        shop.sell(bike)
    
        
    def get_salary(self, salary):
        """ Customer gets some kind of salary and now has a bigger budget for buying bikes"""
        self.budget += salary
        print("{} got salary and now has a budget of ${}".format(self.name, round(self.budget,2)))

