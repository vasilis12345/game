from enemy import Enemy
import random
from rich.console import Console
enemy = Enemy()
from rich import print as rprint


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
                rprint(f"You just [blue]leveled up[/blue]. Your current [blue]level[/blue] is [blue]{self.level}[/blue]")
    def do_attack(self) :
        if self.critical_chance == 1 :
            enemy.enemy_health -= (self.attack * self.critical_damage_multiplier )
            if enemy.enemy_health <= 0 :
                rprint(f"You did [red]{self.attack} damage[/red] and killed [green]{enemy.enemy_type}[/green] with a [red]critical[/red] and gained [blue]{enemy.enemy_xp} xp[/blue]")
                self.xp_held += enemy.enemy_xp
                self.level_up()
                enemy.death_respawn()
            else :
                rprint(f"You did [red]critical damage[/red] to [green]{enemy.enemy_type}[/green] its [green]health[/green] is now [green]{enemy.enemy_health}[/green]")
        else :
            enemy.enemy_health -= self.attack
            if enemy.enemy_health <= 0:
                rprint(f"You did [red]{self.attack} damage[/red] and killed [blue]{enemy.enemy_type}[/blue]. [blue]{enemy.enemy_xp} xp gained[/blue]")
                self.xp_held += enemy.enemy_xp
                self.level_up()
                enemy.death_respawn()
            else :
                rprint(f"You did [red]{self.attack} damage[/red] to [blue]{enemy.enemy_type}[/blue] its [green]health[/green] is now [green]{enemy.enemy_health}[/green]")
    def get_attacked(self) :
        self.health -= enemy.enemy_attack
        if self.health > 0 :
            rprint(f"You got [red]hit[/red] by [blue]{enemy.enemy_type}[/blue] for [red]{enemy.enemy_attack}[/red] now your [green]health[/green] is [green]{self.health}[/green]")
        else :
            rprint(f"You got [red]hit[/red] by [blue]{enemy.enemy_type}[blue] for {BLUE}{enemy.enemy_attack}{RESET} now your {GREEN}health{RESET} is {RED}0{RESET}")
            rprint(f"YOU {RED}DIED{RESET}")
            self.dead = True
    def heal(self) :
        self.health += self.heal_amount
        if self.health > 0 :
            rprint(f"You {GREEN}healed {self.heal_amount} hp{RESET} now your {GREEN}hp{RESET} is {GREEN}{self.health}{RESET}")
        if self.health <= 0 :
            rprint(f"You {GREEN}healed {self.heal_amount} hp{RESET} now your {GREEN}hp{RESET} is {RED}0{RESET}")
            self.dead = True


