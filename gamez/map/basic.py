
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
