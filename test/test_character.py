from typing import ByteString
from character import Character, HealingItem

# teste si le character a 100 hp à sa création
def test_character_hp():
    c = Character("salma")
    assert c.hp == 100

# teste si le character est vivant à sa création
def test_character_is_alive():
    c = Character("salma")
    assert c.is_alive == True

# teste si le character prend des dégâts
def test_character_get_damage():
    c = Character("salma")
    c.get_damage(10)
    assert c.hp == 90

# vérifie si le character peut avoir des dégats négatifs (ne devrait pas)
def test_character_get_damage_negative():
    c = Character("salma")
    try:
        c.get_damage(-10)
    except ValueError as e:
        assert str(e) == "damage should be positive"

# teste si le character meurt quand ses hp sont à 0
def test_character_is_alive_false():
    c = Character("salma")
    c.get_damage(100)
    assert c.is_alive == False

# teste si le character inflige des dégâts à un autre character
def test_character_deal_damage():
    c1 = Character("salma")
    c2 = Character("adrien")
    c1.deal_damage(c2, 10)
    assert c2.hp == 90

# teste si le character peut se soigner
def test_character_heal():
    c = Character("salma")
    c.get_damage(10)
    c.heal(10)
    assert c.hp == 100

# teste si le character ne peut pas avoir plus de hp que son max_hp
def test_character_heal_max_hp():
    c = Character("salma")
    c.get_damage(10)
    c.heal(100)
    assert c.hp == 100

# teste si le character peut avoir des soins négatifs (ne devrait pas)
def test_character_heal_negative():
    c = Character("salma")
    try:
        c.heal(-10)
    except ValueError as e:
        assert str(e) == "heal should be positive"

# teste si le character a un nom
def test_character_name():
    c = Character("salma")
    assert c.name == "salma"

# teste si le character peut boire une potion (HealingItem)
def test_character_drinks_potion():
    c = Character("salma")
    c.get_damage(50)
    c.drink_potion(HealingItem.POTION)
    assert c.hp == 75

# test si le character peut boire une super potion
def test_character_drinks_super_potion():
    c = Character("salma")
    c.get_damage(50)
    c.drink_potion(HealingItem.SUPER_POTION)
    assert c.hp == 100

# test si le character peut boire une hyper potion (et si sa vie après ne dépasse pas 100)
def test_character_drinks_hyper_potion():
    c = Character("salma")
    c.get_damage(50)
    c.drink_potion(HealingItem.HYPER_POTION)
    assert c.hp == 100


# teste si le character peut ajouter une potion à son inventaire
def test_put_potion_into_inventory_valid():
    c = Character("salma")
    c.put_potion_into_inventory(HealingItem.POTION)
    assert HealingItem.POTION in c.inventory


# teste si le character ne peut pas ajouter une potion invalide à son inventaire
def test_put_potion_into_inventory_invalid():
    c = Character("salma")
    try:
        c.put_potion_into_inventory("potion")
    except ValueError as e: 
         assert str(e) == "Invalid potion type"

# teste si le character peut ajouter plusieurs potions à son inventaire
def test_put_potion_into_inventory_multiple():
    c = Character("salma")
    c.put_potion_into_inventory(HealingItem.POTION)
    c.put_potion_into_inventory(HealingItem.SUPER_POTION)
    c.put_potion_into_inventory(HealingItem.HYPER_POTION)
    assert HealingItem.POTION in c.inventory
    assert HealingItem.SUPER_POTION in c.inventory
    assert HealingItem.HYPER_POTION in c.inventory

# teste si le character peut ajouter plus de potions que la taille maximale de son inventaire
def test_put_potion_into_inventory_full():
    c = Character("salma")
    for i in range(5):
        c.put_potion_into_inventory(HealingItem.POTION)
    try:
        c.put_potion_into_inventory(HealingItem.HYPER_POTION)
    except ValueError as e:
        assert str(e) == "Inventory is full"

# teste si le character peut enlever une potion de son inventaire
def test_remove_potion_from_inventory():
    c = Character("salma")
    c.put_potion_into_inventory(HealingItem.POTION)
    c.remove_potion_from_inventory(HealingItem.POTION)
    assert HealingItem.POTION not in c.inventory