# missile_launcher.py
from Weapon_autre import OutOfRangeError
from Weapon_autre import Weapon

class MissileLauncher(Weapon):
    def __init__(self, ammunitions: int, guidance_system):
        # Le rayon d'action est fixé à 100 pour tous les lance-missiles
        super().__init__(ammunitions, 100)
        self.guidance_system = guidance_system

    def is_valid_coordinates(self, x: int, y: int, z: int) -> bool:
        # Vérifier si les coordonnées sont valides pour un lance-missiles
        # Dans cet exemple, on suppose que les missiles ne peuvent être tirés que vers le haut (z > 0)
        return z > 0

    def fire_at(self, x: int, y: int, z: int):
        # Ajout de la vérification du rayon d'action
        if not self.is_valid_coordinates(x, y, z) or not self.is_in_range(x, y, z):
            raise OutOfRangeError("Invalid coordinates or out of range.")
        
        super().fire_at(x, y, z)

    def is_in_range(self, x: int, y: int, z: int) -> bool:
        # Vérifier si la cible est à portée en utilisant le système de guidage
        distance = self.guidance_system.calculate_distance((x, y, z))
        return distance <= self.range

class MockGuidanceSystem:
    def calculate_distance(self, target):
        # Juste une valeur factice pour simuler le calcul de distance
        return 50
