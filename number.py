class Circle(object):
    pi = 3.14
    def __init__(self, radius):
        self.radius = radius

    def circumference(self, diameter):
        # we need to define diameter as intermediary variable
        self.radius * 2 = diameter
        return (Circle.pi * diameter)

x = Circle(radius = 10, diameter = 1)
print(x.circumference())