from character import Character

# teste si le character a 100 hp à sa création
def test_character_hp():
    c = Character()
    assert c.hp == 100

# teste si le character est vivant à sa création
def test_character_is_alive():
    c = Character()
    assert c.is_alive == True

# teste si le character prend des dégâts
def test_character_get_damage():
    c = Character()
    c.get_damage(10)
    assert c.hp == 90

# vérifie si le character peut avoir des dégats négatifs (ne devrait pas)
def test_character_get_damage_negative():
    c = Character()
    try:
        c.get_damage(-10)
    except ValueError as e:
        assert str(e) == "damage should be positive"

# teste si le character meurt quand ses hp sont à 0
def test_character_is_alive_false():
    c = Character()
    c.get_damage(100)
    assert c.is_alive == False

# teste si le character inflige des dégâts à un autre character
def test_character_deal_damage():
    c1 = Character()
    c2 = Character()
    c1.deal_damage(c2, 10)
    assert c2.hp == 90

# teste si le character peut se soigner
def test_character_heal():
    c = Character()
    c.get_damage(10)
    c.heal(10)
    assert c.hp == 100

# teste si le character ne peut pas avoir plus de hp que son max_hp
def test_character_heal_max_hp():
    c = Character()
    c.get_damage(10)
    c.heal(100)
    assert c.hp == 100