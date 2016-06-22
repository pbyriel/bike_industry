from bicycles import *

def main():
    bike1 = Bicycle("Mountain Bike", 6, 500)
    bike2 = Bicycle("Unisex", 7.5, 600)
    bike3 = Bicycle("Racer", 5, 800)
    bike4 = Bicycle("Children's tricycle", 4, 400)
    bike5 = Bicycle("Electric rider", 10, 900)
    bike6 = Bicycle("Boring bike", 8, 150)
    
    customer1 = Customer("Claudia", 200)
    customer2 = Customer("Julia", 500)
    customer3 = Customer("Nana", 1000)
    
    shop_stock = [bike1, bike2, bike3, bike4, bike5, bike6]
    shop = Bike_shop("Bike Living", shop_stock, 15)
    shop.print_status()
    customer1.buy(bike6, shop)
    customer2.buy(bike4, shop)
    customer3.buy(bike3,shop)
    shop.print_status()
    
if __name__=='__main__':
    main()