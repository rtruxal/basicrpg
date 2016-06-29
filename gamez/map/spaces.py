## A1  A2  A3  ..  ..  A15
## B1  B2  B3  ..  ..  B15          N
## C1  C2  C3  ..  ..  C15          |
##                                  |
## .                    .    W<-----O----->E
## .                    .           |
##                                  |
## O1  O2  O3  ..  ..  O15          S


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
        self._id = space_id
        self._alpha_code, self._num_code = self._space_codes()

        self._adj_spaces = {
            'n' : None,
            'e' : None,
            's' : None,
            'w' : None
        }
        self._nearby_grid()

        self._is_perimeter = False
        self.is_perimeter()

        self.terrain = 'BlandLand'
        self.drag = 0

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

    def _nearby_grid(self):
        if self._alpha_code >= 66:
            north = self._alpha_code - 1
            self._adj_spaces['n'] = chr(north) + str(self._num_code)
        if self._alpha_code <= 78:
            south = self._alpha_code + 1
            self._adj_spaces['s'] = chr(south) + str(self._num_code)

        if self._num_code >= 2:
            west = self._num_code - 1
            self._adj_spaces['w'] = chr(self._alpha_code) + str(west)
        if self._num_code <= 14:
            east = self._num_code + 1
            self._adj_spaces['e'] = chr(self._alpha_code) + str(east)

    def is_perimeter(self):
        if self._alpha_code == 65:
            self._is_perimeter = True
        if self._alpha_code == 79:
            self._is_perimeter = True
        if self._num_code == 1:
            self._is_perimeter = True
        if self._num_code == 15:
            self._is_perimeter = True

def create_map_grid():
    from gamez.map.basic import fifteen_by_fifteen as fxf
    spnames = fxf()
    space_dict = {}
    for name in spnames:
        space_dict[name] = GridSpace(name)

    return space_dict






