import numpy as np

def calculate(lst):
    if len(lst) != 9:
        raise ValueError("List must contain nine numbers.")
    
    matrix = np.array(lst).reshape(3, 3)
    
    calculations = {
        'mean': [matrix.mean(axis=0).tolist(), matrix.mean(axis=1).tolist(), matrix.mean().tolist()],
        'variance': [matrix.var(axis=0).tolist(), matrix.var(axis=1).tolist(), matrix.var().tolist()],
        'standard deviation': [matrix.std(axis=0).tolist(), matrix.std(axis=1).tolist(), matrix.std().tolist()],
        'max': [matrix.max(axis=0).tolist(), matrix.max(axis=1).tolist(), matrix.max().tolist()],
        'min': [matrix.min(axis=0).tolist(), matrix.min(axis=1).tolist(), matrix.min().tolist()],
        'sum': [matrix.sum(axis=0).tolist(), matrix.sum(axis=1).tolist(), matrix.sum().tolist()]
    }
    
    return calculations

if __name__ == "__main__":
    import sys
    try:
        # Example test case
        test_list = [0,1,2,3,4,5,6,7,8]
        result = calculate(test_list)
        print(result)
    except Exception as e:
        print(e)

# test_module.py
import unittest

class TestMeanVarStd(unittest.TestCase):
    def test_calculate(self):
        expected_output = {
            'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
            'variance': [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667],
            'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611],
            'max': [[6, 7, 8], [2, 5, 8], 8],
            'min': [[0, 1, 2], [0, 3, 6], 0],
            'sum': [[9, 12, 15], [3, 12, 21], 36]
        }
        self.assertEqual(calculate([0,1,2,3,4,5,6,7,8]), expected_output)

if __name__ == "__main__":
    unittest.main()
