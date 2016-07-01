from gamez.map.gen_maps import create_map_grid
import shelve
from contextlib import closing


def mapdb_input(map_dict):
    assert type(map_dict) is dict, 'input passed to mapdb not dict'
    # import pdb
    # pdb.set_trace()
    with closing(shelve.open('map.db')) as db:
        for key, value in map_dict.items():
            db[key] = value

def mapdb_output_print():
    with closing(shelve.open('map.db', flag='r')) as db:
        for key in db.keys():
            print 'key: {}, value: {}'.format(key, db[key])

def mapdb_output():
    with closing(shelve.open('map.db', flag='r')) as db:
        map_dict = {}
        for key in db.keys():
            print 'key: {}, value: {}'.format(key, db[key])
            map_dict[key] = db[key]
        return map_dict


def instantiate_map():
    active_map = create_map_grid()
    mapdb_input(active_map)
