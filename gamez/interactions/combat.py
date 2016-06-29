#input from powers can be either SPECIAL(list) or INT(damage - pos or neg)
#take into acct two chars health
#turn based.

def combat_c2c(char1, char2):
    print "prepare yourself!"
    print ''
    print "{} and {} HAVE ENTERED THE RING OF MORAL KOMBAT".format(char1.name, char2.name)
    print ''
    raw_input("Press ENTER to proceed.")

    from gamez.powers import get_mage_power_dict
    _mage_powers = get_mage_power_dict()


def sin_wave(x, A=1.0, Pw=1.0, Ps=0.0, b=0.0):
     from math import radians, sin
     func = (A*sin(Pw*radians(x) + Ps) + b)
     return func

def roll_dice():
    from random import randint, random
    from math import pi

    x = random()
    coin_flip = randint(0, 1)
    ps = float()
    if coin_flip == 0:
        ps = 0.0
    elif coin_flip == 1:
        ps = -pi
    else: raise ValueError('something went seriously wrong with randint')

    val = sin_wave(x, Pw=(2.0 * pi), Ps=ps) * 10

    print val