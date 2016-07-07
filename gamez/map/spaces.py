## A1  B1  C1  ..  ..  O1
## A2  B2  C2  ..  ..  O2           N
## A3  B3  C3  ..  ..  O3           |
##                                  |
## .                    .    W<-----O----->E
## .                    .           |
##                                  |
## A15 B15 C15 ..  ..  O15          S


class GridSpace(object):
    # Called with a space ID
    def __init__(self, space_id):
        assert type(space_id) == str, "space_id must be str"
        if len(space_id) == 2:
            pass
        elif len(space_id) == 3:
            pass
        else:
            raise ValueError('space_id not valid')

        # Take in str spaceid and split to int codes
        self._id = space_id
        self._alpha_code, self._num_code = self._space_codes()

        # Currently gives abs values
        self._adj_spaces = {
            'N' : None,
            'E' : None,
            'S' : None,
            'W' : None
        }
        self._nearby_abs()

        # Boolean test referring to entire map-space
        self._is_perimeter = False
        self.is_perimeter()

        # Boolean test referring to sub-sections of map-space
        self._is_section_perimeter = False
        self._adj_door = False
        self._is_quest_space = False
        self._is_dungeon = False
        self._dungeon_name = 'Not a Dungeon'


        self.region = 'badlands'
        self.drag = 0
        self.occupied_by = set()

    def __repr__(self):
        return 'space {}'.format(self._id)

    def _space_codes(self):
        tag = self._id
        letter_val = ord(tag[0])
        number = int(tag[1:])

        # DEBUG
        ## Juuust a little precaution.
        ## whitelists any grid smaller than 15x15
        if number not in [i for i in range(16)]:
            raise ValueError('invalid space ID')
        elif letter_val not in [i for i in range(65, 80)]:
            raise ValueError('invalid space ID')
        else:
            return letter_val, number

    def _nearby_abs(self):
        if self._alpha_code >= 66:
            west = self._alpha_code - 1
            self._adj_spaces['W'] = chr(west) + str(self._num_code)
        if self._alpha_code <= 78:
            east = self._alpha_code + 1
            self._adj_spaces['E'] = chr(east) + str(self._num_code)

        if self._num_code >= 2:
            north = self._num_code - 1
            self._adj_spaces['N'] = chr(self._alpha_code) + str(north)
        if self._num_code <= 14:
            south = self._num_code + 1
            self._adj_spaces['S'] = chr(self._alpha_code) + str(south)




    def is_perimeter(self):
        if self._alpha_code == 65 or 79:
            self._is_perimeter = True
        if self._num_code == 1 or 15:
            self._is_perimeter = True



def create_map_grid(type='default'):
    from gamez.map.gen_maps import fifteen_by_fifteen as fxf
    spnames = fxf()
    space_dict = {}
    for name in spnames:
        space_dict[name] = GridSpace(name)

    return space_dict