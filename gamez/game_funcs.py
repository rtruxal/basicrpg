def plot_func(f, x_range,name=None, _axis=None,  *args, **kwargs):
    import matplotlib.pyplot as plt
    y_bucket = []
    counter = 0
    # import pdb
    # pdb.set_trace()
    for element in x_range:
        y = f(element,*args, **kwargs )
        y_bucket.append(y)
        counter += 1
        # if counter > 9:
        #     break
        if counter == len(x_range[:-10]):

            import pdb
            pdb.set_trace()
    assert len(x_range) == len(y_bucket), "some x values didn't turn into y values or made a buncha extra y values dawg."

    plt.plot(x_range, y_bucket)
    if name is not None:
        plt.ylabel(name)
    if _axis is None:
        plt.axis([-10, 10, -10, 10])
    else:
        assert type(_axis) is list, 'axis value not list'
        x = len(_axis)
        for num in range(x):
            assert type(_axis[num]) is int, 'an axis perameter is not int'
        plt.axis(_axis)
    plt.show()


def sin_wave(X, A=1.0, Pw=1.0, Ps=0.0, b=0.0):
     from math import sin
     f_of_x = (A*sin(Pw*X + Ps) + b)
     return f_of_x


def roll_dice():
    from random import randint, random
    from math import pi

    x = random()
    coin_flip = randint(0, 1)
    pw = None
    b = None
    ps = 0.0

    if coin_flip == 1:
        ps = -pi
    elif coin_flip == 0:
        pass
    else: raise ValueError('something went seriously wrong with randint')

    # Passes 'random' through another ambiguation layer
    # Returns similar result (random float between 0 and 1)
    print 'coinflip:==> ', coin_flip
    print 'x value:==> ', x
    print 'Ps value:==> ', ps
    print 'Pw value:==> ', pw
    print 'b value:==> ', b
    val = sin_wave(x, Pw=(2.0 * pi), Ps=ps)

    print val