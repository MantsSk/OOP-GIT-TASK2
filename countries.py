class Country:
    def __init__(self, name, population, area):
        self.name = name
        self.population = population
        self.area = area
        self.is_big = self.check_if_big()
        self.population_density = self.population / self.area

    def check_if_big(self):
        return self.population > 15000000 or self.area > 3000000

    def compare_population_density(self, other_country):
        if self.population_density > other_country.population_density:
            return f"{self.name} has bigger density as {other_country}"
        elif self.population_density < other_country.population_density:
            return f"{self.name} has less density as {other_country.name}"
        else:
            return f"{self.name} has same density as {other_country.name}"

    def __str__(self):
        return f"{self.name}"

australia = Country("Australia", 23545500, 7692024)
print(australia.is_big)

lithuania = Country("Lithuania",2700000,635000)
print(lithuania.is_big)

spain = Country("Spain", 10000000, 100000000)

print(australia.population_density)
print(lithuania.population_density)
print(lithuania.compare_population_density(australia))
print(australia.compare_population_density(lithuania))
print(lithuania.compare_population_density(lithuania))
print(spain.compare_population_density(australia))