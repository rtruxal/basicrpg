class Item(object):
    def __init__(self, name='rock'):

        self.item_name = name
        self.item_descr = "IDK...It's pretty useless. You could try throwing it as a weapon or eating it...\n\n...\n\n...probably wouldn't end well"

        self.is_consumable = False
        self.is_weapon = False
        self.is_wearable = False
        self.has_sockets = False
        self.is_special = False
        self.quantity = 0



class Weapon(Item):
    def __init__(self, name='bare hands'):
        super(Weapon, self).__init__(name)
        self.is_wearable = True
        self.weap_type = 'unarmed'

class Wearable(Item):
    def __init__(self, name='underoos'):
        super(Wearable, self).__init__(name)
        self.is_wearable = True
        self.wear_type = 'skivvys'

class Consumable(Item):
    def __init__(self, name='air'):
        super(Consumable, self).__init__(name)
        self.is_consumable = True
        self.cons_type = 'nothing'

class Food(Consumable):
    def __init__(self):
        super(Food, self).__init__()
        self.cons_type = 'food'

class Potion(Consumable):
    def __init__(self):
        super(Potion, self).__init__()
        self.cons_type = 'potion'


class Ammo(Consumable):
    def __init__(self):
        super(Ammo, self).__init__()
        self.cons_type = 'ammo'





class Grenade(Consumable, Weapon):
    def __init__(self):
        super(Grenade, self).__init__()
        self.cons_type = 'grenade'
        self.weap_type = 'grenade'

class Sword(Weapon):
    def __init__(self):
        self.weap_type = 'sword'
        super(Sword, self).__init__()
