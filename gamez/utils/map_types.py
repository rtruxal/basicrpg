
def create_map_grid(type='default'):
    from gamez.map.spaces import GridSpace
    from gamez.map.rectangular import fifteen_by_fifteen as fxf
    spnames = fxf()
    space_dict = {}
    for name in spnames:
        space_dict[name] = GridSpace(name)

    return space_dict