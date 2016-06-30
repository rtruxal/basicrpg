def three_person_game():
    from gamez import prompts
    #create heroes
    player1 = None
    player2 = None
    player3 = None
    while True:
        player1 = prompts.prompt_make_char(1)

        player2 = prompts.prompt_make_char(2)

        player3 = prompts.prompt_make_char(3)

        if (player1.chartype and player2.chartype and player3.chartype) == 'blacksmith' or 'mage' or 'spy' or 'dunce':
            break
        else:
            print "let's try this again"
            raw_input('Press Enter to continue.'.upper())
            pass
    print "great success!"
    print "{}, {}, and {} have joined the gamez".format(player1.name, player2.name, player3.name)
    print ''
    raw_input('Press Enter to continue.'.upper())
    return [player1.name, player2.name, player3.name]