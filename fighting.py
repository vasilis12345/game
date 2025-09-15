from enemy import Enemy
from hero import Hero
import readchar
import random
KEY = readchar.key

inventory = []
hero = Hero()
enemy = Enemy()

RED = '\033[91m'
GREEN = '\033[92m'
BLUE = '\033[94m'
RESET = '\033[0m'

def gain_item() :
    chance = random.randint(1 , 100)
    if enemy.enemy_type == "Giant rat" :
        if 50 >= chance >= 25:
            item_gained = True
            inventory.append("paw_boots")
            print("You acquired PAW BOOTS")
            item_gained = False

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

