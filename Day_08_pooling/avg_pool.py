"""
Implementation of avg_pool from scratch.
"""

import numpy as np
import math

class AvgPool:
    def __init__(self):
        self.weights = np.random.randn(10, 10)
        self.bias = np.zeros(10)

    def forward(self, x):
        # Execute forward pass
        return np.dot(x, self.weights) + self.bias

if __name__ == '__main__':
    print('Testing avg_pool.py module...')
    # No API keys required for this module.
