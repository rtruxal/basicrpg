class Item(object):
    def __init__(self):
        self.is_consumable = False
        self.is_weapon = False
        self.is_armor = False
        self.is_special = False
        self.quantity = 0

class Consumable(Item):
    def __init__(self):
        super(Consumable, self).__init__()
        self.is_consumable = True

        self.cons_type = None

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


class Weapon(Item):
    def __init__(self):
        super(Weapon, self).__init__()
        self.is_weapon = True
        self.weap_type = 'bare_hands'


class Grenade(Consumable, Weapon):
    def __init__(self):
        super(Grenade, self).__init__()
        self.cons_type = 'grenade'
        self.weap_type = 'grenade'

class Sword(Weapon):
    def __init__(self):
        self.weap_type = 'sword'
        super(Sword, self).__init__()
