from gamez.character import Hero
from UserDict import UserDict as ud


class CharDict(object):
    ## IT IS A CLASS VARIABLE, NOT PASSED TO INSTANCES.
    ## CHAR DICT IS THE HEART OF THIS.
    ## CURRENT FORMAT IS {'name' : [Hero type, Hero or NPC]}
    _char_dict = ud()

    @classmethod
    def disp(cls):
        print cls._char_dict
    ## So far this @classmethod shit is working. The dude made class methods sound dope,
    ## and I'm hoping I'm being dope also.
    ## This should be like one bucket. There shouldn't be multiple instances
    ## except for new games laterz.
    @classmethod
    def __repr__(cls):
        return 'Character List:\n{}'.format(cls._char_dict)

    @classmethod
    def add_hero_to_dict(cls, name, char):
        if name not in cls._char_dict.keys():
            assert isinstance(char, Hero), "dict value not Hero"
            cls._char_dict[name] = char
            print '{} added to character list.'.format(name)
            raw_input('Press Enter to continue.')
        else:
            print 'Character name taken.\nName not added to character list'
            raw_input('Press Enter to continue.')
            pass

    @classmethod
    def rem_char_from_dict(cls, name):
        if name in cls._char_dict.keys():
            cls._char_dict.__delitem__(name)
            raw_input('{} removed from character list.'.format(name))
        else:
            raw_input('Character name not listed.\nName not removed from character list')
            pass