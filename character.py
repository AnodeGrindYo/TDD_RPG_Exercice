from enum import Enum



class HealingItem(Enum):
    POTION = 25
    SUPER_POTION = 50
    HYPER_POTION = 100


class Character:
    def __init__(self, name):
        return
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
