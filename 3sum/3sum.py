#!/usr/bin/env python
# https://leetcode.com/problems/3sum/
# 3sum.py
# Given an array nums of n integers, are
# there elements a, b, c in nums such that
# a + b + c = 0? Find all unique triplets
# in the array which gives the sum of zero.
# Author: https://github.com/idiego209
# Given array nums = [-1, 0, 1, 2, -1, -4],

# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]

def 3sum(nums):
  """
  Finds unique triplets such that
  their sum is equal to 0.
  Arguments:
    list: nums List of numbers to check.
  Returns:
    list: result List containing unique triplets.
  """
  

def main():
  nums = [-1, 0, 1, 2, -1, -4]

  unique_triplets = 3sum(nums)
  print(unique_triplets)

if __name__ == '__main__':
  main()
