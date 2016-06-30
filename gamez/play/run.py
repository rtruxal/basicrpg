

def place_chars_on_map(map_space_dict, **params):
    from active_players import CharDict
    assert type(map_space_dict) is dict, "map_space_dict is not dict"
    cd = CharDict()._char_dict

    #make an indexed list of perimeter boxes
    poss_starting_points = []
    for label, instan in map_space_dict:
        if instan._is_perimeter == True:
            poss_starting_points.append(instan)

    # Start char on random perimeter space
    from random import randint
    from gamez.interactions.movement import into_space
    for name, hero in cd:
        starting_space = poss_starting_points[randint(0, len(poss_starting_points)-1)]
        into_space(hero, starting_space)


def start_game():
    from gamez.utils.game_types import three_person_game
    from gamez.utils.map_types import create_map_grid
    charlist = three_person_game()
    assert type(charlist) is list, \
        "CHARLIST VARIABLE PASSED FROM GAME_FUNCS.THREE_PERSON_GAME IS NOT A LIST"

    map_space_dict = create_map_grid()







def main():
    pass






if __name__ == '__main__':
    main()