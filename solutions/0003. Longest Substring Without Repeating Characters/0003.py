#!/usr/bin/python3

'''
https://leetcode.com/problems/longest-substring-without-repeating-characters/
'''

from typing import Counter

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        count = Counter()

        l = 0
        for r, c in enumerate(s):
            count[c] += 1
            while count[c] > 1:
                count[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)

        return ans

import unittest

class TestMain(unittest.TestCase):
    def test_func(self):
        s = Solution()
        self.assertEqual(s.lengthOfLongestSubstring("adbabcbb"), 3)
        self.assertEqual(s.lengthOfLongestSubstring("bbbbb"), 1)
        self.assertEqual(s.lengthOfLongestSubstring("pwwkew"), 3)
        self.assertEqual(s.lengthOfLongestSubstring(" "), 1)
        self.assertEqual(s.lengthOfLongestSubstring("aab"), 2)
        self.assertEqual(s.lengthOfLongestSubstring("dvdf"), 3)
        self.assertEqual(s.lengthOfLongestSubstring("aabaab!bb"), 3)

if __name__ == "__main__":
    unittest.main()