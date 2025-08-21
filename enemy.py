import json
import random

with open("config.json") as file:
    data = json.load(file)

enemy_data = data["enemies"]

class Enemy:
    def __init__(self):
        random_spawn = random.choice(list(enemy_data.values()))
        self.id = random_spawn["id"]
        self.enemy_type = random_spawn["enemy_name"]
        self.enemy_attack = random_spawn["attack"]
        self.enemy_health = random_spawn["health"]
        self.enemy_attack_res = random_spawn["attack_res"]
        self.enemy_xp = random_spawn["xp_held"]

