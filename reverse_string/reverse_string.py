#!/usr/bin/env python
# https://leetcode.com/problems/reverse-string/
# reverse_string.py
# Write a function that reverses a string. The input string is given as 
# an array of characters char[]. Do not allocate extra space for another
# array, you must do this by modifying the input array in-place with
# O(1) extra memory. You may assume all the characters consist of
# printable ascii characters.
# Author: https://github.com/idiego209

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        middle = int(len(s)/2)

        for i in range(middle):
            tmp = s[i]
            s[i] = s[-(i + 1)]
            s[-(i + 1)] = tmp
        return s
