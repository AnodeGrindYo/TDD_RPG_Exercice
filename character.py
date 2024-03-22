from enum import Enum
from typing import ByteString



class HealingItem(Enum):
    POTION = 25
    SUPER_POTION = 50
    HYPER_POTION = 100


class Character:
    def __init__(self, name):
        self.hp = 100
        self.is_alive = True
        self.max_hp = 100
        self.name = name
        self.inventory = []


    # recevoir des dégats
    def get_damage(self, damage):
        # vérifie que damae est positif (pas de dégat négatif)
        if damage < 0:
            raise ValueError("damage should be positive")
        self.hp -= damage
        if self.hp <= 0:
            self.is_alive = False

    # infliger des dégats à un autre character
    def deal_damage(self, character, damage):
        character.get_damage(damage)

    # se soigner
    def heal(self, heal):
        # vérifie que heal est positif (pas de soin négatif)
        if heal < 0:
            raise ValueError("heal should be positive")
        if self.hp + heal > self.max_hp:
            self.hp = self.max_hp
        else:
            self.hp += heal

    # boire une potion (vérifier le type de potion et soigner le character en conséquence)
    def drink_potion(self, potion):
        if potion == HealingItem.POTION:
            self.heal(25)
        elif potion == HealingItem.SUPER_POTION:
            self.heal(50)
        elif potion == HealingItem.HYPER_POTION:
            self.heal(100)
        else:
            raise ValueError("Invalid potion type")
        
    # Ajoute une potion à l'inventaire du character
    def put_potion_into_inventory(self, potion):
       if type(potion) != HealingItem:
         raise ValueError("Invalid potion type")
       self.inventory.append(potion)

    # enlever une potion de l'inventaire du character
    def remove_potion_from_inventory(self, potion):
        if type(potion) != HealingItem:
            raise ValueError("Invalid potion type")
        if potion not in self.inventory:
            raise ValueError("Potion not in inventory")
        self.inventory.remove(potion)



