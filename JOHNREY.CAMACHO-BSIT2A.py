class character:
    def __init__(self, name, hero_type):
        self.name = name
        self.hero_type = hero_type

    def __str__(self):
        return "Moskov is a Marksman Hero"

    def describe(self):
        print(f"{self.name} is a {self.hero_type} hero")

hero = character("Moskov" , "Marksman")

print(hero)