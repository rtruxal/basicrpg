from gamez.map.spaces import create_map_grid
import shelve
from contextlib import closing


def mapdb_input_dict(map_dict):
    assert type(map_dict) is dict, 'input passed to mapdb not dict'
    # import pdb
    # pdb.set_trace()
    with closing(shelve.open('map.db')) as db:
        for key, value in map_dict.items():
            db[key] = value

def _mapdb_input_single(gridspace):
    # import pdb
    # pdb.set_trace()
    with closing(shelve.open('map.db')) as db:
        db[gridspace._id] = gridspace

def mapdb_output_print():
    with closing(shelve.open('map.db', flag='r')) as db:
        for key in db.keys():
            print 'key: {}, value: {}'.format(key, db[key])

def mapdb_output():
    with closing(shelve.open('map.db', flag='r')) as db:
        map_dict = {}
        for key in db.keys():
            # print 'key: {}, value: {}'.format(key, db[key])
            map_dict[key] = db[key]
        return map_dict

def mapdb_purge():
    # import pdb
    # pdb.set_trace()
    with closing(shelve.open('map.db')) as mapdb:

        print '*******'
        print 'WARNING'
        print '*******'
        raw_input("DOING THIS WILL WIPE THE LOCAL DATASTORE.")
        response = raw_input("type the letter q to abort.")
        response.lower()
        if response == 'q':
            pass
        else:
            # LET THE PURGING BEGIN.
            for key in mapdb.keys():
                del mapdb[key]
            print 'Contents wiped.'


def instantiate_map():
    active_map = create_map_grid()
    mapdb_input_dict(active_map)
