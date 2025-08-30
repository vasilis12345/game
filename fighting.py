from enemy import Enemy
from hero import Hero,  gain_item

hero = Hero()
enemy = Enemy()

RED = '\033[91m'
GREEN = '\033[92m'
BLUE = '\033[94m'
RESET = '\033[0m'

while not hero.dead:
    character_input =input(f"Will you {RED}attack{RESET} or {GREEN}heal{RESET}??")
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
