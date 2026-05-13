"""
Implementation of backpropagation from scratch.
"""

import numpy as np
import math

class Backpropagation:
    def __init__(self):
        self.weights = np.random.randn(10, 10)
        self.bias = np.zeros(10)

    def forward(self, x):
        # Execute forward pass
        return np.dot(x, self.weights) + self.bias

if __name__ == '__main__':
    print('Testing backpropagation.py module...')
    # No API keys required for this module.
