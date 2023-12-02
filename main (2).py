# main.py
from S2.module1 import Fruit, Vegetable
from S2.module2 import Dish, Beverage

def main():
    # Create instances and demonstrate your code
    apple = Fruit(name="Apple", color="Red")
    banana = Fruit(name="Banana", color="Yellow")

    broccoli = Vegetable(name="Broccoli", is_green=True)
    carrot = Vegetable(name="Carrot", is_green=False)

    pizza = Dish(name="Pizza", cuisine="Italian")
    sushi = Dish(name="Sushi", cuisine="Japanese")

    coffee = Beverage(name="Coffee", type="Hot")
    tea = Beverage(name="Tea", type="Hot")

    # Display information
    print("Fruits:")
    apple.display_info()
    banana.display_info()

    print("\nVegetables:")
    broccoli.display_info()
    carrot.display_info()

    print("\nDishes:")
    pizza.display_info()
    sushi.display_info()

    print("\nBeverages:")
    coffee.display_info()
    tea.display_info()

if __name__ == "__main__":
    main()
