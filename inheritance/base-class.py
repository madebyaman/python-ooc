from abc import ABC, abstractmethod


class GraphicShape(ABC):
    def __init__(self):
        super().__init__()  # Why?

    @abstractmethod
    def calcArea(self):
        pass


class Circle(GraphicShape):
    def __init__(self, radius):
        self.radius = radius

    def calcArea(self):
        return 3.14 * (self.radius ** 2)


c = Circle(5)
print(c.calcArea())
