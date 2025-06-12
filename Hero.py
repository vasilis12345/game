from enemies import Enemies
Enemies = Enemies()
class Hero :
    def __init__(self , health , attack , xp , level , level_req ) :
        self.health = 100
        self.attack = 25
        self.xp = 0
        self.level = 1
        self.level_req = 1000

    def level_up(self) :
        if self.xp == self.level_req :
            self.level +=1
            self.health *= 3
            self.attack += 3
            self.xp = self.xp - self.level_req

    def get_attacked(self, Enemies ) :
        self.health -= Enemies.attack
    def do_attack(self , Enemies ):
        Enemies.health -= self.attack

