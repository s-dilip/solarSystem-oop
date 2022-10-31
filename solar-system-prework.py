#Create a Solar System class
from math import pi

class SolarSystem:

    def __init__(self, stars, planets): #The Constructor
        self.stars = stars
        self.planets = planets

    def add_star(self, star):
        self.stars.append(star)
    
    def add_planet(self, planet):
        self.planets.append(planet)

print("hello world!")

#class Star:

#    def __init__(self, name, mass, temperature): #The constructor
#        self.name = name
#        self.mass = mass
#        self.temperature = temperature




class Planet:

    def __init__(self, name, radius):
      self.name = name
      self.radius = radius

    def circumference(self):
        return (2 *self.radius * pi)



Mars = Planet("Mars", 3389)

solar_sustem = SolarSystem([], [])
solar_sustem.add_planet(Mars)

print(Mars.circumference())
#print(solar_sustem.planets[0].circumference)



    