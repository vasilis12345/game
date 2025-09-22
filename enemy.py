import json
import random

from dulwich.objects import sorted_tree_items

with open("enemy_config.json") as file:
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

sprite_idle  =  "                _                       __\n              /   \\                  /      \\\n             '      \\              /          \\\n            |       |Oo          o|            |\n            `    \\  |OOOo......oOO|   /        |\n             `    \\\\OOOOOOOOOOOOOOO\\//        /\n               \\ _o\\OOOOOOOOOOOOOOOO//. ___ /\n           ______OOOOOOOOOOOOOOOOOOOOOOOo.___\n            --- OO'* `OOOOOOOOOO'*  `OOOOO--\n                OO.   OOOOOOOOO'    .OOOOO o\n                `OOOooOOOOOOOOOooooOOOOOO'OOOo\n              .OO \"OOOOOOOOOOOOOOOOOOOO\"OOOOOOOo\n          __ OOOOOO`OOOOOOOOOOOOOOOO\"OOOOOOOOOOOOo\n         ___OOOOOOOO_\"OOOOOOOOOOO\"_OOOOOOOOOOOOOOOO\n           OOOOO^OOOO0`(____)/\"OOOOOOOOOOOOO^OOOOOO\n           OOOOO OO000/000000\\000000OOOOOOOO OOOOOO\n           OOOOO O0000000000000000 ppppoooooOOOOOO\n           `OOOOO 0000000000000000 QQQQ \"OOOOOOO\"\n            o\"OOOO 000000000000000oooooOOoooooooO'\n            OOo\"OOOO.00000000000000000000OOOOOOOO'\n           OOOOOO QQQQ 0000000000000000000OOOOOOO\n          OOOOOO00eeee00000000000000000000OOOOOOOO.\n         OOOOOOOO000000000000000000000000OOOOOOOOOO\n         OOOOOOOOO00000000000000000000000OOOOOOOOOO\n         `OOOOOOOOO000000000000000000000OOOOOOOOOOO\n           \"OOOOOOOO0000000000000000000OOOOOOOOOOO'\n             \"OOOOOOO00000000000000000OOOOOOOOOO\"\n  .ooooOOOOOOOo\"OOOOOOO000000000000OOOOOOOOOOO\"\n.OOO\"\"\"\"\"\"\"\"\"\".oOOOOOOOOOOOOOOOOOOOOOOOOOOOOo\nOOO         QQQQO\"'                     `\"QQQQ\nOOO\n`OOo.\n  `\"OOOOOOOOOOOOoooooooo.\n\n"
print(sprite_idle)