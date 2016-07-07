from active_players import HeroDict

def place_chars_on_map(map_space_dict, **params):

    # import pdb
    # pdb.set_trace()
    assert type(map_space_dict) is dict, "map_space_dict is not dict"
    cd = HeroDict()


    #make an indexed list of perimeter boxes
    poss_starting_points = []
    for instan in map_space_dict.values():
        if instan._alpha_code == 79 or instan._num_code == 15:
            poss_starting_points.append(instan)

    # Start char on random perimeter space
    from random import randint
    from gamez.interactions.movement import _into_space
    for hero in cd._hero_dict.values():
        starting_space = poss_starting_points[randint(0, len(poss_starting_points)-1)]
        _into_space(hero, starting_space)


def start_game():
    from gamez.utils.game_types import two_person_game
    from active_players import herodb_purge
    herodb_purge()
    hd = HeroDict
    #Can change the line below to ...game_types.X_person_game() where x is one, two, or three
    hero_list = two_person_game()

    assert type(hero_list) is list, \
        "CHARLIST VARIABLE PASSED FROM GAME_FUNCS.THREE_PERSON_GAME IS NOT A list"
    #This instantiates herodb for the game
    hd.add_heroes_to_dict(hero_list)

    from gamez.play.active_map import instantiate_map, mapdb_output
    # instantiate_map takes no arguments as of now
    # eventually I will allow for choosing map types
    instantiate_map()
    map_dict = mapdb_output()
    from gamez.map.gen_maps import fxf_map1
    for spaces in map_dict.values():
        fxf_map1(spaces)
    place_chars_on_map(map_dict)

    #Prove Char persistance, map location, and movement choices
    from pprint import pprint
    for el in hero_list:
        print "{} begins their journey at space {}.".format(el.name, el.current_space_id)
        print "Movement options are as follows: "
        pprint(map_dict[el.current_space_id]._adj_spaces)

    return hero_list


def main():
    start_game()






if __name__ == '__main__':
    main()