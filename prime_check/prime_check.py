#!/usr/bin/env python
# prime_check.py
# Returns True if prime False if not.
# Author: https://github.com/idiego209
def isPrime(num):
  for i in xrange(2, int(num / 2 + 1)):
    if (num % i == 0):
      return False
  return True

def main():
  print(isPrime(3))
  print(isPrime(5))
  print(isPrime(12))

if __name__ == '__main__':
  main()
