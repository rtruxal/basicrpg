def __doc__():

    """
**********************************
    When user-input is needed
**********************************
    prompt_make_char() <====> Hero Creation
        |
        |---takes (<character number>), (return)s <Hero instance>
        |
        |---adds Hero instance to character pool(HeroDict) as {'<name>': <instance>}
        |
        |---checks for name uniqueness



    """

def prompt_make_char(charnum=1):
    from gamez.utils.save import herodb_output, herodb_input, herodb_del_heroes
    from character.character import create_hero_instance
    print "OK player{}. Let's make a character.".format(charnum)
    name = ''

    ## Name a character. Loop until name is unique in HeroDict.
    cd = herodb_output()
    while True:
        name = raw_input("what\'s your name? >")
        if cd == None:
            print 'heroesdb returned None'
            pass
        elif name not in cd.keys():
            break
        else:
            # option to overwrite or rename
            while True:
                print('That name has already been chosen.\n')
                y_or_n = raw_input('Would you like to overwrite the existing character? (y/n)')
                if y_or_n.lower() == 'y':
                    herodb_del_heroes(name)
                    break
                elif y_or_n.lower() == 'n':
                    break
                else:
                    print "PLEASE ENTER A Y OR AN N PLEASE."
                    pass


## Prompt MUST MATCH _choice_dict below.
    print "ok {}, now it's time to pick a class.".format(name)
    print '\n'
    print 'please enter the number corresponding to your hero:'
    print '1: Space-Barbarian'
    print '2: Space-Wizard'
    print '3: Sentinel'
    print '4: Space-Trooper'

    ## Loop to choose a class that exists in _choice_dict.
    ## Change numeric strings to class-names for ease of entry.
    _choice_dict = {'1' : 'blacksmith', '2' : 'mage', '3' : 'spy', '4' : 'soldier', '': 'dunce'}
    choice = ''
    while True:
        choice = raw_input('? => ')
        if choice in _choice_dict.keys():
            break
        else:
            raw_input('That is not a valid choice. Press Enter to try again.')

    ## Instantiate new character.
    new_char = create_hero_instance(name, _choice_dict[choice])
    herodb_input(new_char)
    return new_char

def get_stats(char):
    from character.character import Hero as h
    assert isinstance(char, h), 'Cannot get stats for non-hero'
    return h.stats(char)
