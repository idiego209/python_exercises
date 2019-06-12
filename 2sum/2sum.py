
#!/usr/bin/env python
# https://leetcode.com/problems/two-sum/
# 2sum.py
# Given an array of integers, return indices of the two
# numbers such that they add up to a specific target.
# You may assume that each input would have exactly one
# solution, and you may not use the same element twice.
# Author: https://github.com/idiego209

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sum = {}

        for i, num in enumerate(nums):
            if num not in sum:
                sum[target - num] = i
            else:
                return [sum[num], i]
