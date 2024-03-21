from character import Character

# teste si le character a 100 hp à sa création
def test_character_hp():
    c = Character()
    assert c.hp == 100

# teste si le character est vivant à sa création
def test_character_is_alive():
    c = Character()
    assert c.is_alive == True