#!/usr/bin/python3

'''
https://leetcode.com/problems/add-two-numbers/
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        curr = dummy
        carry = 0

        while carry or l1 or l2:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            curr.next = ListNode(carry % 10)
            carry //= 10
            curr = curr.next

        return dummy.next

import unittest

def array2listnode(arr: list):
    ln = ListNode(0)
    l = ln
    for i in arr:
        l.next = ListNode(i)
        l = l.next
    return ln.next

def listnode2array(ln: ListNode):
    arr = []
    while ln:
        arr.append(ln.val)
        ln = ln.next
    return arr

class TestMain(unittest.TestCase):
    def test_func(self):
        s = Solution()
        lns = (
            ( [2, 4, 3], [5, 6, 4], [7, 0, 8]),
            ( [0], [0], [0]),
            ( [1, 8], [0], [1, 8]),
            ( [5], [5], [0, 1]),
        )
        for l1, l2, l3 in lns:
            l = s.addTwoNumbers(array2listnode(l1), array2listnode(l2))
            self.assertEqual(listnode2array(l), l3)

if __name__ == "__main__":
    unittest.main()