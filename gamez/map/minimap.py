import numpy as np
from matplotlib import pyplot as plt



def make_labels_fxf():
    let_list = [chr(i) for i in range(65, 70)]
    num_list = [i for i in range(1, 16)]
    reg_array = []
    for num in num_list:
        row = []
        for let in let_list:
            foo = let + str(num)
            row.append(foo)
        reg_array.append(row)
    nd_array = np.array(reg_array)
    return nd_array




