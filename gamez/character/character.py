
def __doc__():
    """
****************************
    Character Hierarchy
****************************
    Character
    |
    |---Hero
    |   |
    |   |---SpaceWizard
    |   |
    |   |---SpaceBarbarian
    |   |
    |   |---Sentinel
    |   |
    |   |---Dunce
    |
    |
    |---NPC ##<--Planned
        |
        |---Enemy
            |
            |---Undead
            |
            |---Animal
            |
            |---Human
            |
            |---Boss (can be any previous category)

"""
    pass
## TRANSLATE INDEX QUERIES INTO INSTANTIATIONS
def create_hero_instance(name, class_choice):
    if class_choice == 'mage':
        return SpaceWizard(name)
    elif class_choice == 'blacksmith':
        return SpaceBarbarian(name)
    elif class_choice == 'spy':
        return Sentinel(name)
    elif class_choice == 'soldier':
        return SpaceTrooper(name)
    else:
        print 'Somehow you managed to fuck things up.'
        return Dunce(name)




class Character(object):
    def __init__(self, name):
        self._selectable = False

        self.level = 1
        self.health = 100
        self.dex = 5
        self.stm = 5
        self.str = 5
        self.luck = 5
        self.nice = 5
        self.mana = 150

        self.power1 = None
        self.power2 = None
        self.power3 = None
        self.power4 = None
        self.power5 = None
        self.power6 = None

        self.chartype = None
        self.name = name
        self.inventory = {}
        self.current_space_id = None
        self.money = 0


    def stats(self):
        print "HERE YEEE HERE YEE. NOW PRESENTING THE SUPER AWESOME MEGA DOPE {}.\nHe/She is the Shit.".format(self.name)
        print '----------------------------------------------------'
        print "STATSSTATSSTATSSTATS*STATS*STATSSTATSSTATSSTATSSTATS"
        print '----------------------------------------------------'
        print ''
        print "Character Type: =>", self.chartype
        print "Health: =>", self.health
        print "Dexterity: =>", self.dex
        print "Stamina: =>", self.stm
        print "Strength: =>", self.str
        print "Charisma: =>", self.nice
        print "Luck: =>", self.luck
        print "Mana: =>", self.mana
        print "Power1: =>", self.power1
        print "Power2: =>", self.power2
        print "Power3: =>", self.power3
        print ''
        print 'Standing on location: =>', self.current_space_id
        print 'Money: =>', self.money
        print 'Inventory: ==>', self.inventory

        if not self.power4 == None:
            print "Power4: =>", self.power4
        if not self.power5 == None:
            print "Power5: =>", self.power5
        if not self.power6 == None:
            print "Power6: =>", self.power6
        print '\n'
        raw_input('Press ENTER to continue.'.upper())

    def inventory(self):
        return self.inventory

    def print_name(self):
        print self.name


class Hero(Character):
    def __init__(self, name):
        super(Hero, self).__init__(name)
        self.health += 100
        self._selectable = True


class NPC(Character):
    def __init__(self, type='Blandy McBlanderson'):
        super(NPC, self).__init__(type)
        self.gullibility = 5
        self.unaware_ness = 5
        self.bitchy_ness = 5
        self.scared_ness = 5


class Villager(NPC):
    def __init__(self):
        super(Villager, self).__init__()


class SpaceWizard(Hero):
    def __init__(self, name_input):
        super(SpaceWizard, self).__init__(name_input)
        self.chartype = 'mage'
        self.mana += 150 # now = 300
        self.nice -=1 # now = 4
        self.str -= 1 # now = 4
        self.dex += 3 # now = 8
        self.luck += 1# now = 6
        self.health -= 20 # now = 80
        #self.power1 = 'PLACEHOLDER FOR MAGEPOWERS'
        #self.power2 = 'PLACEHOLDER FOR MAGEPOWERS'
        #self.power3 = 'PLACEHOLDER FOR MAGEPOWERS'

        #self.power4 = 'PLACEHOLDER FOR MAGEPOWERS'
        #self.power5 = 'PLACEHOLDER FOR MAGEPOWERS'
        #self.power6 = 'PLACEHOLDER FOR MAGEPOWERS'


    def __repr__(self):
        return "I\'m a fuckin SPACEWIZARD dawg. The name's {}.".format(self.name)


        pass


class SpaceBarbarian(Hero):
    def __init__(self, name_input):
        super(SpaceBarbarian, self).__init__(name_input)
        self.chartype = 'blacksmith'
        self.health += 50 # now = 150
        self.mana -= 75 # now = 75
        self.str += 4 # now = 9
        self.stm +=2 # now = 7
        #self.power1 = 'PLACEHOLDER FOR BSPOWERS'
        #self.power2 = 'PLACEHOLDER FOR BSPOWERS'
        #self.power3 = 'PLACEHOLDER FOR BSPOWERS'

        #self.power4 = 'PLACEHOLDER FOR BSPOWERS'
        #self.power5 = 'PLACEHOLDER FOR BSPOWERS'
        #self.power6 = 'PLACEHOLDER FOR BSPOWERS'

    def __repr__(self):
        return "{} SMASH!".format(self.name)


class Sentinel(Hero):
    def __init__(self, name_input):
        super(Sentinel, self).__init__(name_input)
        self.chartype = 'spy'
        self.mana += 50 # now = 200
        self.str -= 1 # now = 4
        self.stm += 3 # now = 8
        self.dex += 5 # now = 10
        self.luck += 2 # now = 7
        #self.power1 = 'PLACEHOLDER FOR BSPOWERS'
        #self.power2 = 'PLACEHOLDER FOR BSPOWERS'
        #self.power3 = 'PLACEHOLDER FOR BSPOWERS'

        #self.power4 = 'PLACEHOLDER FOR BSPOWERS'
        #self.power5 = 'PLACEHOLDER FOR BSPOWERS'
        #self.power6 = 'PLACEHOLDER FOR BSPOWERS'

    def __repr__(self):
        return "No body gonna hear ya die in space boiiiii. If I had a name, it would be {}.".format(self.name)


class Dunce(Hero):
    def __init__(self, name_input):
        super(Dunce, self).__init__(name_input)
        self.chartype = 'dunce'
        self.mana -= 149 # now = 1
        self.str += 20 # now = 25
        self.dex -= 4 # now = 1
        self.luck += 5 # now = 10
        self.health -= 50 # now 50
        self.nice -=3 # now 2
        #self.power1 = 'PLACEHOLDER FOR DUMBPOWERS'
        #self.power2 = 'PLACEHOLDER FOR DUMBPOWERS'
        #self.power3 = 'PLACEHOLDER FOR DUMBPOWERS'

        #self.power4 = 'PLACEHOLDER FOR DUMBPOWERS'
        #self.power5 = 'PLACEHOLDER FOR DUMBPOWERS'
        #self.power6 = 'PLACEHOLDER FOR DUMBPOWERS'

class SpaceTrooper(Hero):
    def __init__(self, name_input):
        super(SpaceTrooper, self).__init__(name_input)
        self.chartype = 'dunce'
        self.mana -= 75 # now = 75
        self.dex += 3 # now = 8
        self.luck += 3 # now = 8
        self.stm += 3 # now 8
        #self.power1 = 'PLACEHOLDER FOR DUMBPOWERS'
        #self.power2 = 'PLACEHOLDER FOR DUMBPOWERS'
        #self.power3 = 'PLACEHOLDER FOR DUMBPOWERS'

        #self.power4 = 'PLACEHOLDER FOR DUMBPOWERS'
        #self.power5 = 'PLACEHOLDER FOR DUMBPOWERS'
        #self.power6 = 'PLACEHOLDER FOR DUMBPOWERS'

    def __repr__(self):
        return "YAAAAAAY EARTHWORMS. IM {} AND IM INTELAGENT.".format(self.name)


def main():
    pass
if __name__ == '__main__':
    main()


