class NoAmmunitionError(Exception):
    pass

class OutOfRangeError(Exception):
    pass

class Weapon:
    def __init__(self, ammunitions: int, range: int):
        self.ammunitions = ammunitions
        self.range = range      
        
    def fire_at(self, x: int, y: int, z: int):
        pass 
    
class MissileSurface(Weapon):
    def fire_at(self, x: int, y: int, z: int):
        if self.ammunitions == 0:
            raise NoAmmunitionError("Plus de munitions disponibles")
        if z != 0:
            self.ammunitions -= 1
            raise OutOfRangeError("Coordonnées de la cible invalides pour Missile antisurface")
        else:
            print(f"Tir de Missile antisurface aux coordonnées ({x}, {y}, {z})")
            self.ammunitions -= 1

class MissileAntiAir(Weapon):
    def fire_at(self, x: int, y: int, z: int):
        if self.ammunitions == 0:
            raise NoAmmunitionError("Plus de munitions disponibles")
        if z <= 0:
            self.ammunitions -= 1
            raise OutOfRangeError("Coordonnées de la cible invalides pour Missile anti-air")
        else:
            print(f"Tir de Missile anti-air aux coordonnées ({x}, {y}, {z})")
            self.ammunitions -= 1

class Torpedo(Weapon):
    def fire_at(self, x: int, y: int, z: int):
        if self.ammunitions == 0:
            raise NoAmmunitionError("Plus de munitions disponibles")
        if z > 0:
            self.ammunitions -= 1
            raise OutOfRangeError("Coordonnées de la cible invalides pour Torpille")
        else:
            print(f"Tir de Torpille aux coordonnées ({x}, {y}, {z})")
            self.ammunitions -= 1
