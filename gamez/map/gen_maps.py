from gamez.map.spaces import GridSpace


def fifteen_by_fifteen():

    letters = [chr(a) for a in range(65, 80)]
    numbers = [str(i + 1) for i in range(15)] # + 1 so starts with 'A1'

    space_ids = []
    for char in letters:
        for num in numbers:
            space_ids.append(char + num)

    ## space_ids are a list of 15X15 tiles
    ## format is [[A1, A2,..., A15], ..., [O1, O2,..., O15]]
    return space_ids

def fxf_map1(Space):
    # ADD A LITTLE COLOR TO YOUR LIFE
    # TAKES NORMAL 15 X 15 MAP AND CREATES MAP IN FILE:
    # gamez.Square_Map_Design_15x15.xlsx

    from gamez.map.spaces import GridSpace
    assert isinstance(Space, GridSpace), 'arg passed to fxf_map1 not GridSpace. cannot overlay map characteristics.'
    #dungeons
    secret_passage = ['B6', 'C6']
    abandoned_outpost = ['A13', 'A14', 'B13', 'B14']
    abandoned_runway = ['E11', 'E12', 'E13', 'E14']
    royal_guard_quarters = ['F2', 'F3', 'F4', 'G2', 'G3', 'G4', 'H2', 'H3', 'H4']
    rebel_citadel = ['G12', 'G13', 'H12', 'H13', 'I12', 'I13']
    space_bear_cave = ['L1', 'L2', 'M1', 'M2']
    forest_o_lazers = ['M4', 'M5', 'N4', 'N5']
    rebel_outpost = ['M8', 'M9', 'M10', 'N10']

    #rows a thru e
    if Space._alpha_code <= 69:

        # Give map region
        if Space._num_code <= 5:
            Space.region = 'Space-Palace'
        elif Space._num_code <= 10:
            Space.region = 'Market'
        else:
            Space.region = 'Badlands'

        # lay quest-spaces, is-dungeon, and adj-doors
        if Space._id == 'A1':
            # A1 -> final boss
            Space._is_quest_space = True
        elif Space._id in secret_passage:
            Space._is_dungeon = True
            Space._dungeon_name = 'Secret Passage'
            if Space._id == 'B6':
                Space._adj_door = True
                Space._is_quest_space = True
        elif Space._id in abandoned_outpost:
            Space._is_dungeon = True
            Space._dungeon_name = 'Abandoned Outpost'
        elif Space._id in abandoned_runway:
            Space._is_dungeon = True
            Space._dungeon_name = 'Abandoned Runway'
        # for doors not in dungeons
        elif Space._id in ['E3', 'B5', 'C10', 'C11']:
            Space._adj_door = True


    elif Space._alpha_code <= 74:
        # Map regions
        if Space._num_code <= 5:
            Space.region = 'Barracks'
        elif Space._num_code <= 10:
            Space.region = 'Village'
        else:
            Space.region = 'Badlands'

        # quest-spaces, is-dungeon, and adj-doors
        if Space._id == 'J8':
            # Only adj-door or quest-spaces in this sector that isn't
            # part of a dungeon
            Space._adj_door = True
        elif Space._id in royal_guard_quarters:
            Space._is_dungeon = True
            Space._dungeon_name = 'Quarters of The Royal Guard'
            if Space._id == 'G3':
                Space._is_quest_space = True
            if Space._id == 'F3':
                Space._adj_door = True
        elif Space._id in rebel_citadel:
            Space._is_dungeon = True
            Space._dungeon_name = 'Rebel Citadel'
            if Space._id == 'H12':
                Space._is_quest_space = True

    else:
        # Map region (only one)
        Space.region = 'Badlands'

        # quest-spaces, is-dungeon, and adj-doors
        if Space._id == 'K8':
            Space._adj_door = True
        elif Space._id in space_bear_cave:
            Space._is_dungeon = True
            Space._dungeon_name = 'SPACE-BEAR CAVE'
            if Space._id == 'M1':
                Space._is_quest_space = True
        elif Space._id in forest_o_lazers:
            Space._is_dungeon = True
            Space._dungeon_name = "Forest 'o Lazers"
        elif Space._id in rebel_outpost:
            Space._is_dungeon = True
            Space._dungeon_name = 'Rebel Outpost'

    def _nearby_rel(Space):
        assert isinstance(Space, GridSpace), 'arg passed to fxf_map1 not GridSpace. cannot overlay map characteristics.'

        if Space._adj_door == True:
            pass
        elif Space._num_code <= 5:
            if Space._num_code == 5 and Space._alpha_code <= 69:
                Space._adj_spaces['S'] = 'A WALL'
            if Space._alpha_code == 69 or Space._alpha_code == 74:
                Space._adj_spaces['E'] = 'A WALL'
            elif Space._alpha_code == 70 or Space._alpha_code == 75:
                Space._adj_spaces['W'] = 'A WALL'

        elif Space._num_code <= 10:
            if Space._num_code == 6 and Space._alpha_code <= 69:
                Space._adj_spaces['N'] = 'A WALL'
            if Space._num_code == 10 and Space._alpha_code <=74:
                Space._adj_spaces['S'] = 'A WALL'
            if Space._alpha_code == 74:
                Space._adj_spaces['E'] = 'A WALL'
            elif Space._alpha_code == 75:
                Space._adj_spaces['W'] = 'A WALL'

        elif Space._num_code <= 15:
            if Space._num_code == 11 and Space._alpha_code <= 74:
                Space._adj_spaces['N'] = 'A WALL'

    _nearby_rel(Space)
    from gamez.utils.save import _mapdb_input_single as inp
    inp(Space)


def create_map_grid(type='default'):
    spnames = fifteen_by_fifteen()
    space_dict = {}
    for name in spnames:
        space_dict[name] = GridSpace(name)

    return space_dict