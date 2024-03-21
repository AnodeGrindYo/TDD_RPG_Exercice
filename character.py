class Character:
    def __init__(self):
        self.hp = 100
        self.is_alive = True

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