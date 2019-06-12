#!/usr/bin/env python
# https://leetcode.com/problems/to-lower-case/
# to_lower_case.py
# Implement function ToLowerCase() that has a
# string parameter str, and returns the same
# string in lowercase.
# Author: https://github.com/idiego209

class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        offset = ord('a') - ord('A')
        for i, c in enumerate(str):
            if ord('A') <= ord(c) <= ord('Z'):
                str = str[:i] + chr(ord(c) + offset) + str[i+1:]
        return str
