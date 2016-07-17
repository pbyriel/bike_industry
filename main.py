from bicycles import *

def main():
    sports = Sportsbikes()
    citybikes = Citybikes()
    bike1 = sports.make_mountain_bike()
    bike2 = sports.make_racing_bike()
    bike3 = sports.make_pro_bike()
    bike4 = citybikes.make_child_bike()
    bike5 = citybikes.make_electric_bike()
    bike6 = citybikes.make_urban_bike()
    
    customer1 = Customer("Claudia", 200)
    customer2 = Customer("Julia", 500)
    customer3 = Customer("Nana", 1000)
    
    shop = Bike_shop("Bike Living", [], 6000, 25)
    shop.buy([bike1, bike2, bike3, bike4, bike5, bike6])
    shop.print_status()
    customer1.buy(bike6, shop)
    customer2.buy(bike4, shop)
    customer3.buy(bike3, shop)
    shop.print_status()
    
if __name__=='__main__':
    main()