from enemy import Enemy
from hero import Hero
import readchar
import random
KEY = readchar.key
from rich import print as rprint

inventory = []
hero = Hero()
enemy = Enemy()
hero.kill_count = 0
RED = '\033[91m'
GREEN = '\033[92m'
BLUE = '\033[94m'
RESET = '\033[0m'


def fight() :
    while not hero.dead:
        character_input =input(f"Will you {RED}attack{RESET} or {GREEN}heal{RESET}??\n")
        if character_input == "attack" :
            hero.do_attack()
            if enemy.enemy_health <= 0 :
                hero.kill_count += 1
            hero.get_attacked()
        elif character_input == "heal" :
            hero.heal()
            hero.get_attacked()
        else :
            rprint("Please enter a possible move")

