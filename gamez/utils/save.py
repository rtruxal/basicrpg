import shelve
from contextlib import closing

def herodb_input(*hero_inst):
    from gamez.character.character import Hero

    # import pdb
    # pdb.set_trace()
    with closing(shelve.open('heroes.db')) as herodb:
        for inst in hero_inst:
            assert isinstance(inst, Hero), 'item(s) in var list not all Heroes'
            herodb[inst.name] = inst

def herodb_input_dict(hero_dict):
    assert type(hero_dict) is dict, 'input passed to herodb not dict'
    # import pdb
    # pdb.set_trace()
    with closing(shelve.open('heroes.db')) as herodb:
        for key, value in hero_dict.items():
            herodb[key] = value


def herodb_del_heroes(hero_names):
    # import pdb
    # pdb.set_trace()
    with closing(shelve.open('heroes.db')) as herodb:
        for key in hero_names:
            print "You are about to remove {} from the hero_list. This cannot be undone.".format(key)
            response = raw_input("type the letter q to abort removal")
            if response == 'q':
                pass
            else:
                del herodb[key]


def herodb_purge():
    # import pdb
    # pdb.set_trace()
    with closing(shelve.open('heroes.db')) as herodb:

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
            for key in herodb.keys():
                del herodb[key]
            print 'Contents wiped.'


def herodb_output_print():
    import os
    direct = os.getcwd()
    if os.path.exists(os.path.join(direct, 'heroes.db')) == False:
        print 'HERODB DOES NOT EXIST'
        with closing(shelve.open('heroes.db')) as herodb:
            for key in herodb.keys():
                print 'key: {}, value: {}'.format(key, herodb[key])
    else:
        with closing(shelve.open('heroes.db', flag='r')) as herodb:
            for key in herodb.keys():
                print 'key: {}, value: {}'.format(key, herodb[key])


def herodb_output():
    import os
    direct = os.getcwd()
    if os.path.exists(os.path.join(direct, 'heroes.db')) == False:
        print 'HERODB DOES NOT EXIST. Instantiating'
        _herodb_instantiate()
        return {}
    else:
        with closing(shelve.open('heroes.db', flag='r')) as herodb:
            hero_dict = {}
            for key in herodb.keys():
                hero_dict[key] = herodb[key]
            return hero_dict


def _herodb_instantiate():
    with closing(shelve.open('heroes.db')) as db:
        pass


def _mapdb_instantiate():
    with closing(shelve.open('map.db')) as db:
        pass


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