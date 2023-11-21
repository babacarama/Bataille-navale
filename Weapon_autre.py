class NoAmmunitionError(Exception):
    pass

class OutOfRangeError(Exception):
    pass

class Weapon:
    def __init__(self, ammunitions: int, weapon_range: int):
        self.ammunitions = ammunitions
        self.range = weapon_range      

    def fire_at(self, x: int, y: int, z: int):
        if self.ammunitions == 0:
            raise NoAmmunitionError("No ammunition available.")

        if not self.is_valid_coordinates(x, y, z):
            raise OutOfRangeError("Invalid coordinates.")

        self.ammunitions -= 1
        print(f"Firing at coordinates ({x}, {y}, {z}).")

    def is_valid_coordinates(self, x: int, y: int, z: int) -> bool:
        # Méthode à implémenter dans les sous-classes
        pass
