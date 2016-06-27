#input from powers can be either SPECIAL(list) or INT(damage - pos or neg)
#take into acct two chars health
#turn based.

def combat_c2c(char1, char2):
    print "prepare yourself!"
    print ''
    print "{} and {} HAVE ENTERED THE RING OF MORAL KOMBAT".format(char1.name, char2.name)
    print ''
    raw_input("Press ENTER to proceed.")

    from powers import get_mage_power_dict
    _mage_powers = get_mage_power_dict()
