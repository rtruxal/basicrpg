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
    from gamez.play.active_players import HeroDict as cd
    from character import create_hero_instance
    print "OK player{}. Let's make a character.".format(charnum)
    name = ''

    ## Name a character. Loop until name is unique in HeroDict.
    while True:
        name = raw_input("what\'s your name? >")
        if name not in cd._hero_dict.keys():
            break
        else:
            raw_input('That name has already been chosen. Press Enter to try again.')

    ## Prompt MUST MATCH _choice_dict below.
    print "ok {}, now it's time to pick a class.".format(name)
    print '\n'
    print 'please enter the number corresponding to your hero:'
    print '1: Blacksmith'
    print '2: Mage'
    print '3: Spy'

    ## Loop to choose a class that exists in _choice_dict.
    ## Change numeric strings to class-names for ease of entry.
    _choice_dict = {'1' : 'blacksmith', '2' : 'mage', '3' : 'spy', '': 'dunce'}
    choice = ''
    while True:
        choice = raw_input('? => ')
        if choice in _choice_dict.keys():
            break
        else:
            raw_input('That is not a valid choice. Press Enter to try again.')

    ## Instantiate new character.
    new_char = create_hero_instance(name, _choice_dict[choice])
    hd = cd()
    cd.add_hero_to_dict(new_char)
    print cd._hero_dict
    return new_char

def get_stats(char):
    from character import Hero as h
    assert isinstance(char, h), 'Cannot get stats for non-hero'
    return h.stats(char)
