import numpy as np
from numpy.typing import NDArray


class Solution:
    
    def sigmoid(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array
        # Formula: 1 / (1 + e^(-z))
        # return np.round(your_answer, 5)
        pass
        value = []
        for ele in z:
            value.append(round(1 / (1 + (math.e ** -ele)), 5))
        return value

    def relu(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array
        # Formula: max(0, z) element-wise
        pass
        value = []
        for ele in z:
            value.append(round(max(0.0, ele), 5))
        return value
