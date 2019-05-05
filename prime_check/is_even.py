#!/usr/bin/env python
# is_even.py
# Returns True if even False if not.
# Author: https://github.com/idiego209
def isEven(num):
  """
  Determines if number passed is even or odd.
  Arguments:
    int: num Number given as input.
  Returns:
    True for even False for odd
  """
  if num % 2 == 0:
    return True
  else:
    return False

def main():
  print(isEven(2))
  print(isEven(5))

if __name__ == '__main__':
  main()
