"""
started:
-------

character file:
    contains all character class objects. 3 levels of character hirearchy.
    Class structure:
        character[Hero[Herotype]] or character[NPC[NPCtype]] etc...


    contains dict class which holds 1 key to a 2 element list:
        {'<name>' : [<hero or npc>, <herotype or npctype etc..>]}


prompt file:
    so far just a character creation prompt.
        asks and passes name and herotype


powers file:
    comprised of function definitions describing attacks/actions

    takes 2 args
        a hero instance
        a str command refering to power chosen

    returns either an int or a string.
        if int is returned, health/barrier destruction is the subject
        if str is returned, things are more open ended.


index file:
    main commands

#################################################################################
#################################################################################

TODO:
    make a map

    make a cohesive character to character interaction framework
        needs to be more robust than just 'if str then' do some shit.

    make items
    make inventory for heroes
    determine/define item scope of influence

    create character level framework











"""