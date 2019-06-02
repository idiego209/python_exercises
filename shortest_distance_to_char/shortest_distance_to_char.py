#!/usr/bin/env python
# https://leetcode.com/problems/shortest-distance-to-a-character/
# shortest_distance_to_char.py
# Given a string S and a character C, return an array of
# integers representing the shortest distance from the
# character C in the string.
# Author: https://github.com/idiego209

class Solution(object):
    def IntToChar(self, substring, C):
        int_to_C = 0

        for char in substring:
            if char == C:
                return int_to_C
            else:
                int_to_C += 1
        return int_to_C

    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        prev_val = len(S)
        current_val = 0
        substring_index = 0
        result = []

        for char in S:
            substring = S[substring_index:]
            if C not in substring:
                result.append(prev_val)
                prev_val += 1
                substring_index += 1
                continue
            else:
                current_val = self.IntToChar(substring, C)
                if current_val == 0:
                    result.append(0)
                    prev_val = 0
                elif current_val < prev_val:
                    result.append(current_val)
                else:
                    result.append(prev_val)
            substring_index += 1
            prev_val += 1
        return result


