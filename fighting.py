from enemy import Enemy
from hero import Hero,  gain_item
import readchar

KEY = readchar.key

hero = Hero()
enemy = Enemy()

RED = '\033[91m'
GREEN = '\033[92m'
BLUE = '\033[94m'
RESET = '\033[0m'

def fight() :
    while not hero.dead:
        character_input =input(f"Will you {RED}attack{RESET} or {GREEN}heal{RESET}??")
        if character_input == "attack" :
            hero.do_attack()
            if enemy.enemy_health <= 0 :
                gain_item()
                hero.kill_count += 1
            hero.get_attacked()
        elif character_input == "heal" :
            hero.heal()
            hero.get_attacked()
        else :
            print("Please enter a possible move")

