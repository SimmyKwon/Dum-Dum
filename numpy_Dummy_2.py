#! /usr/bin/env python

import numpy as np
from numpy import random

huge_array_1 = np.array([[[[2,3],[5,7]],[[11,19],[13,17]],[[1,4],[9,16]]],
                          [[[1,2],[3,4]],[[5,6],[7,8]],[[10,11],[12,13]]]])

huge_rand_array_1 = np.random.rand(2,3,2,2)
huge_rand_array_2 = np.random.rand(2,3,2,2)


print(huge_array_1 + huge_rand_array_1)
print(huge_array_1 - huge_rand_array_2)

print(huge_rand_array_1 @ huge_rand_array_2)
