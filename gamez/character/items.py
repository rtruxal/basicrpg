class Item(object):
    def __init__(self, name=None, descr=None, value=0):
        assert type(name) == (str or None)
        assert type(descr) == (str or None)
        assert type(value) == int

        if name == None:
            self.name = 'Sand'
        else: self.name = name

        if descr == None:
            self.descr = "something went wrong in the mess that is my item creation scheme"
        else: self.descr = descr

        self.is_consumable = False
        self.is_weapon = False
        self.is_wearable = False
        self.has_sockets = False
        self.is_special = False
        self.value = value



class Weapon(Item):
    def __init__(self, name='bare hands', descr=None, value=0, weap_type='unarmed'):
        assert type(weap_type) == str
        super(Weapon, self).__init__(name, descr, value)
        self.is_wearable = True
        self.weap_type = weap_type

class Wearable(Item):
    def __init__(self, name='underoos', descr=None, value=0, wear_type='skivvys'):
        assert type(wear_type) == str
        super(Wearable, self).__init__(name, descr, value)
        self.is_wearable = True
        self.wear_type = wear_type

class Consumable(Item):
    def __init__(self, name='air', descr=None, value=0, cons_type='empty space'):
        assert type(cons_type) == str
        super(Consumable, self).__init__(name, descr, value)
        self.is_consumable = True
        self.cons_type = cons_type



class Food(Consumable):
    def __init__(self, name=None):
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
