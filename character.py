class Character:
    def __init__(self):
        self.hp = 100
        self.is_alive = True

    def get_damage(self, damage):
        self.hp -= damage
        