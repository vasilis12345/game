from enemy import Enemy
from Hero import Hero
import random

hero = Hero(attack=25 , health=100 , xp_req=1000 , xp_held=0 , critical_chance=random.randint(1 , 100) , critical_damage_multiplier=1.9 ,level=1 )
enemy = Enemy()


