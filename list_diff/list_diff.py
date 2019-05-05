#!/usr/bin/env python
# list_diff.py
# Given two lists with one item in difference return diff element.
# Author: https://github.com/idiego209
# Assume input provided is two lists of ints.
# No repeating numbers only one element is different.

def findDiffSets(complete_list, partial_list):
  diff_element = set(complete_list) - set(partial_list)
  assert (len(diff_element) >= 1)
  return list(diff_element)[0]

def findDiffLists(complete_list, partial_list):
  diff_element = sum(complete_list) - sum(partial_list)
  return diff_element

def findDiffXor(complete_list, partial_list):
  xor_sum = 0
  for num in complete_list:
    xor_sum ^= num
  for num in partial_list:
    xor_sum ^= num
  return xor_sum

def main():
  complete_list = [5, 2, 3, 4]
  partial_list = [5, 2, 3]

  print(findDiffSets(complete_list, partial_list))
  print(findDiffLists(complete_list, partial_list))
  print(findDiffXor(complete_list, partial_list))

if __name__ == '__main__':
  main()
