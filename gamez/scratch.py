# def nearby():
#         tag = 'A41'
#         letter = tag[0]
#         number = int(tag[1:])
#         print letter, 'type==>', type(letter)
#         print number, 'type==>', type(number)
#
# nearby()


# def create_map_grid():
#     from gamez.map.basic import fifteen_by_fifteen as fxf
#     from gamez.map.spaces import GridSpace
#     from UserDict import UserDict as ud
#
#     spnames = fxf()
#     space_dict = ud()
#
#     for name in spnames:
#         space_dict[name] = GridSpace(name)
#
#     return space_dict


# make sure the plotting function takes
#     - an f(x) = def
#     -
#     -
from math import pi

from gamez.game_funcs import plot_func, sin_wave

rangez = [i/100.0 for i in range(-100, 101)]

plot_func(sin_wave, rangez, name='Sin Wave', Pw=2.0*pi)


