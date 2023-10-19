class Weapon:
    def __init__(self, ammunitions: int, range: int):
        self.ammunitions = ammunitions
        self.range = range
    def fire_at(self, x: int, y: int, z: int):
        print(f"Firing at coordinates({x}, {y}, {z})") 
