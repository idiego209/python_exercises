#!/usr/bin/env python
# string_to_int.py
# Given a string of digits return a number.
# Assume input is a positive or negative number.
# No whitespaces, empty input, or letters.
# Author: https://github.com/idiego209

def string_to_int(s):
  index = 0
  isNeg = False
  num = 0

  if s[0] == '-':
    isNeg = True
    s = s[1:]
  for c in s:
    num += (ord(c) - ord('0')) * (10**(len(s) - 1 - index))
    index += 1
  if isNeg:
    num = num * -1
  return num

def main():
  test1 = '403'
  test2 = '-487'
  test3 = '139089'

  print(string_to_int(test1))
  print(string_to_int(test2))
  print(string_to_int(test3))

if __name__ == '__main__':
  main()
