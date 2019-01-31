class Nation:

    def __init__(self, name, continent, population, land):
        self.name = name
        self.continent = continent
        self.population = population
        self.land = land

    def popDensity(self, population, land):
        return int(self.population) / float(self.land)
