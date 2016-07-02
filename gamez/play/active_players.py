from gamez.character import Hero
import shelve
from contextlib import closing

def herodb_input(hero_dict):
    assert type(hero_dict) is dict, 'input passed to herodb not dict'
    # import pdb
    # pdb.set_trace()
    with closing(shelve.open('heroes.db')) as herodb:
        for key, value in hero_dict.items():
            herodb[key] = value

def herodb_del_heroes(hero_name_list):
    assert type(hero_name_list) is list, 'input passed to herodb not list'
    # import pdb
    # pdb.set_trace()
    with closing(shelve.open('heroes.db')) as herodb:
        for key in hero_name_list:
            print "You are about to remove {} from the hero_list. This cannot be undone.".format(key)
            response = raw_input("type the letter q to abort removal")
            if response == 'q':
                pass
            else:
                del herodb[key]


def herodb_purge():
    # import pdb
    # pdb.set_trace()
    with closing(shelve.open('heroes.db')) as herodb:

        print '*******'
        print 'WARNING'
        print '*******'
        raw_input("DOING THIS WILL WIPE THE LOCAL DATASTORE.")
        response = raw_input("type the letter q to abort.")
        response.lower()
        if response == 'q':
            pass
        else:
            # LET THE PURGING BEGIN.
            for key in herodb.keys():
                del herodb[key]
            print 'Contents wiped.'


def herodb_output_print():
    with closing(shelve.open('heroes.db', flag='r')) as herodb:
        for key in herodb.keys():
            print 'key: {}, value: {}'.format(key, herodb[key])

def herodb_output():
    with closing(shelve.open('heroes.db', flag='r')) as herodb:
        hero_dict = {}
        for key in herodb.keys():
            print 'key: {}, value: {}'.format(key, herodb[key])
            hero_dict[key] = herodb[key]
        return hero_dict

# THIS WHOLE CLASS IS PRETTY SUPERFLUOUS NOW THAT I'VE FOUND SHELVE
class HeroDict(object):
    ## IT IS A CLASS VARIABLE, NOT PASSED TO INSTANCES.
    ## CHAR DICT IS THE HEART OF THIS.
    ## CURRENT FORMAT IS {'name' : [Hero type, Hero or NPC]}
    _hero_dict = {}

    @classmethod
    def disp(cls):
            herodb_output_print()

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
        for hero in heroes[0]:
            if hero.name not in cls._hero_dict.keys():
                assert isinstance(hero, Hero), "dict value not Hero"
                cls._hero_dict[hero.name] = hero
            else:
                print 'Character name taken.\nName not added to character list'
                raw_input('Press Enter to continue.')
                pass
        herodb_input(cls._hero_dict)

    @classmethod
    def rem_hero_from_dict(cls, name=None):
        if name in cls._hero_dict.keys():
            cls._hero_dict.__delitem__(name)
            herodb_del_heroes([name])
        else:
            raw_input('Character name not listed.\nName not removed from character list')
            pass

