#!/usr/bin/env python
# int_to_next_char.py
# Given a string and key char return list
# of integers shwoing distance of each char
# in string to key char.
# Author: https://github.com/idiego209

def getIntToNextChar(partial_string, C):
  int_to_C = 0

  for char in partial_string:
    if char == C:
      return int_to_C
    else:
      int_to_C += 1

def iterString(S, C):
  int_to_next = []
  pointer_in_string = 0

  if C not in S:
    print("{} is not in {}").format(C, S)
    return None
  for char in S:
    partial_string =S[pointer_in_string:]
    if C in partial_string:
      int_to_next.append(getIntToNextChar(partial_string, C))
      pointer_in_string += 1
  return int_to_next

def main():
  S = 'ilovethisgame'
  C = 'e'

  print(iterString(S, C))

if __name__ == '__main__':
  main()
