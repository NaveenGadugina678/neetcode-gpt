import numpy as np
from numpy.typing import NDArray


class Solution:

    def softmax(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array of logits
        # Hint: subtract max(z) for numerical stability before computing exp
        # return np.round(your_answer, 4)
        pass
        result = []
        total = 0
        max_z = max(z)
        for ele in z:
            total += np.exp(ele - max_z) 


        for ele in z:
            value = (np.exp(ele - max_z)) / total
            result.append(round(value, 4))

        return result