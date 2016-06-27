

def print_mage_power_dict():
    from pprint import pprint
    mage_powers = {
        'petrify' : "Takes 60 mana. | Basically you stop somebody. They lose a turn cuz you makum all immobile. pretty self-splanitory.",
        'blast' : "Takes 50 mana & does 25 magic dmg | Iits a fierballs",
        'burst': "takes 25 mana and does 10 damage",
        'heal' : "takes 25 mana and does -25 damage"
    }
    pprint(mage_powers)
    pass

def get_mage_power_dict():
    mage_powers = {
        'petrify' : "Takes 60 mana. | Basically you stop somebody. They lose a turn cuz you makum all immobile. pretty self-splanitory.",
        'blast' : "Takes 50 mana & does 25 magic dmg | Iits a fierballs",
        'burst': "takes 25 mana and does 10 damage",
        'heal' : "takes 25 mana and does -25 damage"
    }
    return mage_powers


def fuckin_mage_power(mage, power):
## TAKES A HERO INSTANCE AND A POWER REFERENCE.
## DOES A SERIES OF CHECKS 'BOUT MANA AND COMMAND ACCURACY.
## CAN DEAL DAMAGE OR DO OTHER SHIT -- DAMAGE IS ALWAYS AN INT, SPECIAL IS A STR (maybe make it a list)
    from gamez.character import Mage as m
    assert isinstance(mage, m)
    damage = 0
    special = ''
    if power == 'petrify':
        if mage.mana >= 60:
            mage.mana -= 60
            special += 'petrify'
            print "Didn't think I was serious when I said I was half spider, did you?"
            print "You're welcome."
        else:
            print 'not enough mana'
            pass
    elif power == 'blast':
        if mage.mana >= 50:
            mage.mana -= 50
            damage = 25
            print "FIREBAL."
        else:
            print 'not enough mana'
            pass
    elif power == 'burst':
        if mage.mana >= 25:
            mage.mana -= 25
            damage = 10
            print "Burst a' magic shit blasts out your hands."
        else:
            print 'not enough mana'
            pass
    elif power == 'heal':
        if mage.mana >= 25:
            mage.mana -= 25
            damage = -25
            print "shhhhh. It's totally fine...I'm a doctor."
        else:
            print 'not enough mana'
            pass
    else:
        print 'You mutter words but they are not magic.'

## IF INT IS RETURNED, DAMAGE OR HEALTH IS DEALT
    if bool(damage) == True:
        print 'Your {} spell did {} damage.'.format(power, damage)
        return damage
## IF STR IS RETURNED, SOMETHING ELSE HAPPENS
    if bool(special) == True:
        print 'A {} spell leaves your...(some sort of magic stick)'.format(special)
        return special

def fuckin_blacksmith_power(Blacksmith, power):
    damage = 0
    mana_before = Blacksmith.mana
    if Blacksmith.health <= 35:
        raw_input("FUCK THIS YOU'RE PISSED. NO BODY FUCK'S WITH THE BLACKSMITH ON A BAD DAY.")
        print "YOU WANNA FUCK WITH ME?!?! DO YOU KNOW WHO i MOTHAFUCKIN AM??? I'M {}...BITCH.".format(Blacksmith.name)
        raw_input("U DEAD NAH.")
        Blacksmith.mana += 100
        print '**(your mana has increased by 100pts)**'
    else: pass
    if power == 'swing':
        if Blacksmith.mana >= 10:
            Blacksmith.mana -= 10
            damage = 15
        else:
            print 'not enough mana'
            pass
    elif power == 'berzerk':
        if Blacksmith.mana >= 125:
            Blacksmith.mana -= 125
            damage = 100
        else:
            print 'not enough mana'
            pass
    elif power == 'rage_face':
        if Blacksmith.mana >= 170:
            Blacksmith.mana -= 170
            damage = -25
        else:
            print 'not enough mana'
            pass
    else:
        print 'Wow dude. That was an awful swing. Just terrible.'
        raw_input('...')
        raw_input('..')
        raw_input('')
        raw_input('')
        print 'Try and do better.'
        raw_input('')
    print 'Your {} spell did {} damage.'.format(power, damage)

    if mana_before > Blacksmith.mana:
        Blacksmith.mana = (mana_before - 15)
    else: pass
    return damage

