from enemies import Enemies
from Hero import Hero

Hero = Hero()
Enemies = Enemies()
print(Enemies.health)
Hero.do_attack(Enemies)
print(Enemies.health)
