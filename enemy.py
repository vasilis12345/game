import json
import random

with open("config.json") as file:
    data = json.load(file)

enemy_data = data["enemies"]



class Enemy:
    def __init__(self):
        self.random_spawn = random.choice(list(enemy_data.values()))
        self.id = self.random_spawn["id"]
        self.enemy_type = self.random_spawn["enemy_name"]
        self.enemy_attack = self.random_spawn["attack"]
        self.enemy_health = self.random_spawn["health"]
        self.enemy_attack_res = self.random_spawn["attack_res"]
        self.enemy_xp = self.random_spawn["xp_held"]
    def death_respawn(self):
        self.random_spawn = random.choice(list(enemy_data.values()))
        self.id = self.random_spawn["id"]
        self.enemy_type = self.random_spawn["enemy_name"]
        self.enemy_attack = self.random_spawn["attack"]
        self.enemy_health = self.random_spawn["health"]
        self.enemy_attack_res = self.random_spawn["attack_res"]
        self.enemy_xp = self.random_spawn["xp_held"]
        print(f"a {self.enemy_type} just spawned")


