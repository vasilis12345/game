from enemy import Enemy
from Hero import Hero

hero = Hero()
enemy = Enemy()


while not hero.dead:
    character_input =input("Will you attack or heal??")
    if character_input == "attack" :
        hero.do_attack()
        hero.get_attacked()
        hero.gain_item()
    elif character_input == "heal" :
        hero.get_attacked()
        hero.heal()
    else :
        print("Please enter a possible move")
