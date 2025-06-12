import random
death = False
class Enemies :
    def __init__(self ,  name ,attack , health , attack_res , xp_held , en_type) :
        en_type = Rat(health=35, attack=9, attack_res=0, xp_held=120)
    def do_attack(self) :
        pass
    def get_attacked(self) :
        pass
    def death(self) :
        while death == True :
            rand = random.randint(1 , 2)
            if rand == 1 :
                en_type = Rat(health=35,attack=9,attack_res=0,xp_held=120)
            elif rand == 2 :
                en_type = Wild_Dog(health=51,attack=13,attack_res=0,xp_held=0)

class Rat :
    def __init__(self , attack , health , attack_res , xp_held) :
        self.health = 35
        self.attack = 9
        self.attack_res = 0
        self.xp_held = 120
    def do_attack(self) :
        pass
    def get_attacked(self) :
        pass

class Wild_Dog :
    def __init__(self, attack, health, attack_res, xp_held) :
        self.attack = 13
        self.health = 51
        self.attack_res = 0
        self.xp_held = 220

