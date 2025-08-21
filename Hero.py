from enemy import Enemy
import random
enemy = Enemy()


class Hero :
    def __init__(self , attack , health , level , xp_req , xp_held , critical_chance) :
        self.attack = 25
        self.health = 100
        self.xp_req = 1000
        self.xp_held = 0
        self.level = 1
        self.critical_chance = random.randint(1 , 100)
    def level_up(self) :
        if  self.xp_req >= self.xp_held :
            self.level += 1
            self.attack += 5
            self.health += 25
            self.critical_chance = random.randint(1 , self.level - 101)
            self.xp_held -= self.xp_req
            self.xp_req += 250
    def do_attack(self) :

        enemy.enemy_health -= self.attack
        print(f"Y")
    def get_attacked(self) :
        self.health -= enemy.enemy_attack
        print(f"You got hit by {enemy.enemy_type} for -{enemy.enemy_attack} now your health is {self.health}")
        if self.health < 0 :
            print("You died")
