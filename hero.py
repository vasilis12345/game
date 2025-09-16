from enemy import Enemy
import random
enemy = Enemy()


RED = '\033[91m'
GREEN = '\033[92m'
BLUE = '\033[94m'
RESET = '\033[0m'

class Hero :
    def __init__(self) :
        self.attack = 25
        self.health = 100
        self.xp_req = 1000
        self.xp_held = 0
        self.level = 1
        self.critical_chance = random.randint(1 , 100)
        self.critical_damage_multiplier = 1.9
        self.heal_amount = self.health / 10
        self.dead = False
        self.kill_count = 0
    def level_up(self) :
            if self.xp_held >= self.xp_req:
                self.level += 1
                self.attack += 5
                self.health += 25
                self.critical_chance = random.randint(1, max(1, self.level))
                self.critical_damage_multiplier += 0.3
                self.xp_held -= self.xp_req
                self.xp_req += 250
                print(f"You just {BLUE}leveled up{RESET}. Your current {BLUE}level{RESET} is {BLUE}{self.level}{RESET}")
    def do_attack(self) :
        if self.critical_chance == 1 :
            enemy.enemy_health -= (self.attack * self.critical_damage_multiplier )
            if enemy.enemy_health <= 0 :
                print(f"You did {RED}{self.attack} damage{RESET} and killed {GREEN}{enemy.enemy_type}{RESET} with a {RED}critical{RESET} and gained {BLUE}{enemy.enemy_xp} xp{RESET}")
                self.xp_held += enemy.enemy_xp
                self.level_up()
                enemy.death_respawn()
            else :
                print(f"You did {RED}critical damage{RESET} to {GREEN}{enemy.enemy_type}{RESET} its {GREEN}health{RESET} is now {GREEN}{enemy.enemy_health}{RESET}")
        else :
            enemy.enemy_health -= self.attack
            if enemy.enemy_health <= 0:
                print(f"You did {RED}{self.attack} damage{RESET} and killed {GREEN}{enemy.enemy_type}{RESET}. {BLUE}{enemy.enemy_xp} xp gained{RESET}")
                self.xp_held += enemy.enemy_xp
                self.level_up()
                enemy.death_respawn()
            else :
                print(f"You did {RED}{self.attack} damage{RESET} to {BLUE}{enemy.enemy_type}{RESET} its {GREEN}health{RESET} is now {GREEN}{enemy.enemy_health}{RESET}")
    def get_attacked(self) :
        self.health -= enemy.enemy_attack
        if self.health > 0 :
            print(f"You got {RED}hit{RESET} by {BLUE}{enemy.enemy_type}{RESET} for {RED}{enemy.enemy_attack}{RESET} now your {GREEN}health{RESET} is {GREEN}{self.health}{RESET}")
        else :
            print(f"You got {RED}hit{RESET} by {BLUE}{enemy.enemy_type}{RESET} for {BLUE}{enemy.enemy_attack}{RESET} now your {GREEN}health{RESET} is {RED}0{RESET}")
            print(f"YOU {RED}DIED{RESET}")
            self.dead = True
    def heal(self) :
        self.health += self.heal_amount
        if self.health > 0 :
            print(f"You {GREEN}healed {self.heal_amount} hp{RESET} now your {GREEN}hp{RESET} is {GREEN}{self.health}{RESET}")
        if self.health <= 0 :
            print(f"You {GREEN}healed {self.heal_amount} hp{RESET} now your {GREEN}hp{RESET} is {RED}0{RESET}")
            self.dead = True


