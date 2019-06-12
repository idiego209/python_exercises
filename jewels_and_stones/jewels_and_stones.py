#!/usr/bin/env python
# https://leetcode.com/problems/jewels-and-stones/
# jewels_and_stones.py
# You're given strings J representing the types of stones
# that are jewels, and S representing the stones you have.
# Each character in S is a type of stone you have.  You
# want to know how many of the stones you have are also jewels.
# The letters in J are guaranteed distinct, and all characters
# in J and S are letters. Letters are case sensitive, so "a" is
# considered a different type of stone from "A".
# Author: https://github.com/idiego209

class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        jewels = 0

        for c in S:
            if c in J:
                jewels += 1
        return jewels
