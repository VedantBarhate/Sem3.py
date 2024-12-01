
class Superhero:
    def __init__(self,name, power, kills):
        self.name = name
        self.power = power
        self.kills = kills

    def __add__(self, other):
        new_name = self.name + other.name
        new_power = self.power + other.power
        new_kills = self.kills + other.kills
        return Superhero(new_name, new_power, new_kills)

    def __str__(self):
        return f"Name: {self.name}, Power: {self.power}, Kills: {self.kills}"


superman = Superhero("Superman", 90, 20)
batman = Superhero("Batman", 90, 25)

superbat = superman+batman

print("SuperBat features:-")
print(superbat)
print(" Name: ", superbat.name)
print(" Power: ", superbat.power)
print(" Kills: ", superbat.kills)