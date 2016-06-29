# def nearby():
#         tag = 'A41'
#         letter = tag[0]
#         number = int(tag[1:])
#         print letter, 'type==>', type(letter)
#         print number, 'type==>', type(number)
#
# nearby()


def create_map_grid():
    from gamez.map.basic import fifteen_by_fifteen as fxf
    from gamez.map.spaces import GridSpace
    from UserDict import UserDict as ud

    spnames = fxf()
    space_dict = ud()

    for name in spnames:
        space_dict[name] = GridSpace(name)

    return space_dict

