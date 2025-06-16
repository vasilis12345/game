import random

is_dead = True
class Enemies :
    def __init__(self) :
        if is_dead == True :
            en_choice = random.randint(1 , 2)
            if en_choice == 1 :
                is_dead = False
                def Raat() :
                    return Rat(35 , 9  , 0 , 120)
            elif en_choice == 2 :
                is_dead = False
                def Wild_doog() :
                    return Wild_Dog(13 , 51 , 0 , 220 )







class Rat :
    def __init__(self , attack , health , attack_res , xp_held) :
        self.health = 35
        self.attack = 9
        self.attack_res = 0
        self.xp_held = 120


class Wild_Dog :
    def __init__(self, attack, health, attack_res, xp_held) :
        self.attack = 13
        self.health = 51
        self.attack_res = 0
        self.xp_held = 220
