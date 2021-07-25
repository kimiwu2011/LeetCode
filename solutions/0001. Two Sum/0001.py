#!/usr/bin/python3
from typing import List

'''
https://leetcode.com/problems/two-sum/
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numToIndex = {}
        for i, num in enumerate(nums):
            if (target - num) in numToIndex:
                return [numToIndex[target - num], i]
            numToIndex[num] = i

import unittest

class TestMain(unittest.TestCase):
    def test_func(self):
        s = Solution()
        self.assertEqual(s.twoSum([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(s.twoSum([3, 2, 4], 6), [1, 2])
        self.assertEqual(s.twoSum([3, 3], 6), [0, 1])

if __name__ == "__main__":
    unittest.main()