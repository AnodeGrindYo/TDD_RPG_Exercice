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