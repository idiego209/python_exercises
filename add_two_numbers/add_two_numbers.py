#!/usr/bin/env python
# https://leetcode.com/problems/add-two-numbers/
# add_two_numbers.py
# You are given two non-empty linked lists representing two
# non-negative integers. The digits are stored in reverse
# order and each of their nodes contain a single digit. Add
# the two numbers and return it as a linked list.
# Author: https://github.com/idiego209

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        val = 0
	carry = 0
	actual = 0
	sum = ListNode(None)
        sum_head = sum

        while (l1 != None or l2 != None):
            if (l1 != None and l2 != None):
                actual = l1.val + l2.val
                l1 = l1.next
                l2 = l2.next
            elif (l1 != None):
                actual = l1.val
                l1 = l1.next
            else:
                actual = l2.val
                l2 = l2.next
            val = actual % 10
            if (val + carry != 10):
                sum.next = ListNode(val + carry)
                carry = val / 10
            else:
                sum.next = ListNode(0)
            sum = sum.next
        if (carry != 0):
            sum.next = NodeList(carry)
        return sum_head.next
