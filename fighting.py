from enemy import Enemy
from hero import Hero,  gain_item

hero = Hero()
enemy = Enemy()


while not hero.dead:
    character_input =input("Will you attack or heal??")
    if character_input == "attack" :
        hero.do_attack()
        if enemy.enemy_health <= 0 :
            gain_item()
        hero.get_attacked()
    elif character_input == "heal" :
        hero.get_attacked()
        hero.heal()
    else :
        print("Please enter a possible move")
