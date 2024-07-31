class fruit:
    def __init__(self, fruit) -> None:
        self.fruit = fruit


class Apple:
    def __init__(self, color, size) -> None:
        self.color = color
        self.size = size


# apple = Apple("Red", "Medium")
# print(Apple)  ### Address of Apple

f = fruit(Apple)
print(f.fruit)
