from character import Character

# teste si le character a 100 hp à sa création
def test_character_hp():
    c = Character()
    assert c.hp == 100