from enemy import Enemy
import random
enemy = Enemy()

class Hero :
    def __init__(self) :
        self.attack = 25
        self.health = 100
        self.xp_req = 1000
        self.xp_held = 0
        self.level = 1
        self.critical_chance = random.randint(1 , 100)
        self.critical_damage_multiplier = 1.9
        self.heal_amount = self.health / 25
        self.dead = False
    def level_up(self) :
            if self.xp_held >= self.xp_req:
                self.level += 1
                self.attack += 5
                self.health += 25
                self.critical_chance = random.randint(1, max(1, self.level))
                self.critical_damage_multiplier += 0.3
                self.xp_held -= self.xp_req
                self.xp_req += 250
                print(f"You just leveled up. Your current level is {self.level}")
    def do_attack(self) :
        if self.critical_chance == 1 :
            enemy.enemy_health -= (self.attack * self.critical_damage_multiplier )
            if enemy.enemy_health <= 0 :
                print(f"You did {self.attack} damage and killed {enemy.enemy_type} with a critical and gained {enemy.enemy_xp} xp")
                self.xp_held += enemy.enemy_xp
                self.level_up()
                enemy.death_respawn()
            else :
                print(f"You did critical damage to {enemy.enemy_type} its health is now {enemy.enemy_health}")
        else :
            enemy.enemy_health -= self.attack
            if enemy.enemy_health <= 0:
                print(f"You did {self.attack} damage and killed {enemy.enemy_type} and gained {enemy.enemy_xp} xp")
                self.xp_held += enemy.enemy_xp
                self.level_up()
                enemy.death_respawn()
            else :
                print(f"You did damage to {enemy.enemy_type} its health is now {enemy.enemy_health}")
    def get_attacked(self) :
        self.health -= enemy.enemy_attack
        print(f"You got hit by {enemy.enemy_type} for -{enemy.enemy_attack} now your health is {self.health}")
        if self.health < 0 :
            print("You died")
            self.dead = True
    def heal(self) :
        self.health += self.heal_amount
        print(f"You healed {self.heal_amount} hp")
