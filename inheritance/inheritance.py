class Car:
    def __init__(self, name, company, year):
        self.name = name
        self.company = company
        self.year = year


class ElectricCar(Car):
    def __init__(self, name, company, year, battery):
        super().__init__(name, company, year)
        self.batter = battery
