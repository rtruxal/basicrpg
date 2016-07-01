from active_players import HeroDict

def place_chars_on_map(map_space_dict, **params):

    # import pdb
    # pdb.set_trace()
    assert type(map_space_dict) is dict, "map_space_dict is not dict"
    cd = HeroDict()


    #make an indexed list of perimeter boxes
    poss_starting_points = []
    for instan in map_space_dict.values():
        if instan._is_perimeter == True:
            poss_starting_points.append(instan)

    # Start char on random perimeter space
    from random import randint
    from gamez.interactions.movement import _into_space
    for hero in cd._hero_dict.values():
        starting_space = poss_starting_points[randint(0, len(poss_starting_points)-1)]
        _into_space(hero, starting_space)


def start_game():

    from gamez.utils import game_types

    hd = HeroDict
    #change below to ...game_types.X_person_game() where x is one, two, or three
    hero_list = game_types.two_person_game()

    assert type(hero_list) is list, \
        "CHARLIST VARIABLE PASSED FROM GAME_FUNCS.THREE_PERSON_GAME IS NOT A list"
    #This instantiates a MapDict for the game
    print hd.add_heroes_to_dict(hero_list)
    print HeroDict._hero_dict
    from gamez.play.active_map import active_map
    x = active_map
    place_chars_on_map(x)


    for el in hero_list:
        print active_map[el.current_space_id]._adj_spaces





def main():
    start_game()






if __name__ == '__main__':
    main()