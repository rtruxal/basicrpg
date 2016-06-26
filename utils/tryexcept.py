def main():
    import numpy as np
    try:
        h = int(raw_input('gimme triangle height:\n'))
        b =  int(raw_input(("gimme da base\n")))
    except ValueError:
        print 'u smrt'
        exit()

    try:
        h / b
        b / h
        pass
    except ZeroDivisionError:
        print "You're a fucking liar dude."
        exit()

    z = np.sqrt(h**2 + b**2)
    print "hurrs the hypotenuse: ", z, '\n'

    area = ((0.5 * b) * h)
    print "hurrs the volume dawg", area, '\n'







if __name__ == '__main__':
    main()
