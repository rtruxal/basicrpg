from gamez.map.gen_maps import create_map_grid
from gamez.utils.save import mapdb_input_dict


def instantiate_map():
    active_map = create_map_grid()
    mapdb_input_dict(active_map)
