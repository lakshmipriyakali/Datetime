class Dish:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

    def display_info(self):
        print(f"{self.name} - {self.cuisine} cuisine")


class Beverage:
    def __init__(self, name, type):
        self.name = name
        self.type = type

    def display_info(self):
        print(f"{self.name} - {self.type} beverage")