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

    def show_info(self):
        print(f"Enemy: {self.enemy_type}")
        print(f"ID: {self.id}")
        print(f"Attack: {self.enemy_attack}")
        print(f"Health: {self.enemy_health}")
        print(f"Attack Resistance: {self.enemy_attack_res}")
        print(f"XP: {self.enemy_xp}")

# Example usage:
enemy = Enemy()
enemy.show_info()
