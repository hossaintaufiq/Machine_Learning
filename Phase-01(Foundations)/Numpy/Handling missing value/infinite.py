#np.isinf() 10^1000
#1/0

import numpy as np

arr= np.array([1, 2, np.inf, 4, 5, -np.inf])

print(np.isinf(arr))    