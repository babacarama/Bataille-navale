# missile_launcher.py
from Weapon_autre import Weapon

class MissileLauncher(Weapon):
    def __init__(self, ammunitions: int, weapon_range: int, guidance_system):
        super().__init__(ammunitions, weapon_range)
        self.guidance_system = guidance_system

    def is_valid_coordinates(self, x: int, y: int, z: int) -> bool:
        # Vérifier si les coordonnées sont valides pour un lance-missiles
        # Dans cet exemple, on suppose que les missiles ne peuvent être tirés que vers le haut (z > 0)
        return z > 0

class MockGuidanceSystem:
    def calculate_distance(self, target):
        # Juste une valeur factice pour simuler le calcul de distance
        return 50
