from gamez.character.character import Hero


# THIS WHOLE CLASS IS PRETTY SUPERFLUOUS NOW THAT I'VE FOUND SHELVE
class HeroDict(object):
    ## IT IS A CLASS VARIABLE, NOT PASSED TO INSTANCES.
    ## CHAR DICT IS THE HEART OF THIS.
    ## CURRENT FORMAT IS {'name' : [Hero type, Hero or NPC]}
    _hero_dict = {}

    @classmethod
    def disp(cls):
            print cls._hero_dict.keys()

    ## So far this @classmethod shit is working. The dude made class methods sound dope,
    ## and I'm hoping I'm being dope also.
    ## This should be like one bucket. There shouldn't be multiple instances
    ## except for new games laterz.
    @classmethod
    def __repr__(cls):
        return 'Character List:\n{}'.format(cls._hero_dict)

    @classmethod
    def add_hero_to_dict(cls, hero):
        if hero.name not in cls._hero_dict.keys():
            assert isinstance(hero, Hero), "dict value not Hero"
            cls._hero_dict[hero.name] = hero
            print '{} added to character list.'.format(hero.name)
            raw_input('Press Enter to continue.')
        else:
            print 'Character name taken.\nName not added to character list'
            raw_input('Press Enter to continue.')
            pass

    @classmethod
    def add_heroes_to_dict(cls, *heroes):
        for hero in heroes:
            if hero.name not in cls._hero_dict.keys():
                assert isinstance(hero, Hero), "dict value not Hero"
                cls._hero_dict[hero.name] = hero
            else:
                print 'Character name taken.\nName not added to character list'
                raw_input('Press Enter to continue.')
                pass


    @classmethod
    def rem_hero_from_dict(cls, name=None):
        if name in cls._hero_dict.keys():
            cls._hero_dict.__delitem__(name)
        else:
            raw_input('Character name not listed.\nName not removed from character list')
            pass

