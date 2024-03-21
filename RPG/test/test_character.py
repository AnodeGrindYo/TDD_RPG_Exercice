from character import Character

# vérifie qu'un personnage a 100pt de vie à sa création
def test_character_has_100_hp():
    character = Character()
    assert character.hp == 100