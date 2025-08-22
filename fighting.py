from enemy import Enemy
from Hero import Hero
import keyboard

hero = Hero()
enemy = Enemy()

while hero.dead == False :
   enemy.death_respawn()
   if keyboard.is_pressed("a") :
       hero.do_attack()
   elif keyboard.is_pressed("h") :
       hero.heal()
   hero.get_attacked()

