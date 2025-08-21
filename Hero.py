from enemy import Enemy
import random
enemy = Enemy()


class Hero :
    def __init__(self , attack , health , level , xp_req , xp_held , critical_chance , critical_damage_multiplier) :
        self.attack = 25
        self.health = 100
        self.xp_req = 1000
        self.xp_held = 0
        self.level = 1
        self.critical_chance = random.randint(1 , 100)
        self.critical_damage_multiplier = 1.9
    def level_up(self) :
        if  self.xp_req >= self.xp_held :
            self.level += 1
            self.attack += 5
            self.health += 25
            self.critical_chance = random.randint(1 , self.level - 101)
            self.critical_damage_multiplier += 0.3
            self.xp_held -= self.xp_req
            self.xp_req += 250
    def do_attack(self) :
        if self.critical_chance == 1 :
            enemy.enemy_health -= (self.attack * self.critical_damage_multiplier )
            if enemy.enemy_health <= 0 :
                print(f"You killed {enemy.enemy_type} with a critical and gained {enemy.enemy_xp}")
                enemy.death_respwan()
            else :
                print(f"You did critical damage to {enemy.enemy_type} its health is now {enemy.enemy_health}")
        else :
            enemy.enemy_health -= self.attack
            if enemy.enemy_health <= 0:
                print(f"You killed {enemy.enemy_type} and gained {enemy.enemy_xp}")
            else :
                print(f"You did damage to {enemy.enemy_type} its health is now {enemy.enemy_health}")

    def get_attacked(self) :
        self.health -= enemy.enemy_attack
        print(f"You got hit by {enemy.enemy_type} for -{enemy.enemy_attack} now your health is {self.health}")
        if self.health < 0 :
            print("You died")
