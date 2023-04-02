
from abc import ABC, abstractmethod

"""
Usage:
This abstract base class can be used by any class to indicate that it has a method to represent itself in JSON.
"""


class JSONify(ABC):
    @abstractmethod
    def toJSON(self):
        pass


class GraphicShape(ABC):
    def __init__(self):
        super().__init__()  # Why?

    @abstractmethod
    def calcArea(self):
        pass


class Circle(GraphicShape, JSONify):
    def __init__(self, radius):
        self.radius = radius

    def calcArea(self):
        return 3.14 * (self.radius ** 2)

    def toJSON(self):
        return f"{{\"Circle \": {str(self.calcArea())} }}"


c = Circle(10)
print(c.toJSON())
