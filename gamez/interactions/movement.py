def _into_space(character, space):

    from gamez.character import Character
    from gamez.map.spaces import GridSpace
    assert isinstance(character, Character), '1st argument "character" not Character instance'
    assert isinstance(space, GridSpace), '2nd argument "character" not GridSpace instance'

    space.occupied_by.add(character.name)
    character.current_space_id = space._id

def _outof_space(character, space):

    from gamez.character import Character
    from gamez.map.spaces import GridSpace
    assert character.name in space.occupied_by, 'shit'
    assert isinstance(character, Character), '1st argument "character" not Character instance'
    assert isinstance(space, GridSpace), '2nd argument "character" not GridSpace instance'

    space.occupied_by.remove(character.name)
