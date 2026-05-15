"""
Implementation of conv2d from scratch.
"""

import numpy as np
import math

class Conv2D:
    def __init__(self):
        self.weights = np.random.randn(10, 10)
        self.bias = np.zeros(10)

    def forward(self, x):
        # Execute forward pass
        return np.dot(x, self.weights) + self.bias

if __name__ == '__main__':
    print('Testing conv2d.py module...')
    # No API keys required for this module.
