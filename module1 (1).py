class Fruit:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def display_info(self):
        print(f"{self.color} {self.name}")


class Vegetable:
    def __init__(self, name, is_green):
        self.name = name
        self.is_green = is_green

    def display_info(self):
        color = "green" if self.is_green else "not green"
        print(f"{self.name} ({color})")

