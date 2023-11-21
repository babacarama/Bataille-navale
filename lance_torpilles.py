# torpedo_launcher.py
from Weapon_autre import OutOfRangeError, Weapon

class TorpedoLauncher(Weapon):
    def __init__(self, ammunitions: int):
        # Le rayon d'action est fixé à 40 pour le lance-torpilles
        super().__init__(ammunitions, 40)

    def is_valid_coordinates(self, x: int, y: int, z: int) -> bool:
        # Vérifier si les coordonnées sont valides pour un lance-torpilles
        # Dans cet exemple, on suppose que les torpilles peuvent être tirées dans n'importe quelle direction
        return True

    def fire_at(self, x: int, y: int, z: int):
        # Ajout de la vérification du rayon d'action
        if not self.is_valid_coordinates(x, y, z) or not self.is_in_range(x, y, z):
            raise OutOfRangeError("Invalid coordinates or out of range.")
        
        super().fire_at(x, y, z)

    def is_in_range(self, x: int, y: int, z: int) -> bool:
        # Les torpilles ont un rayon d'action fixe, la vérification est donc basée sur la distance
        distance = ((x**2) + (y**2) + (z**2))**0.5
        return distance <= self.range
