#!/usr/bin/env python
# fibonacci.py
# Fibinacci sequence generator.
# Author: https://github.com/idiego209

def fibGenerator(seq_length):
  a, b = 0, 1

  for _ in xrange(seq_length):
    yield a
    a, b = b, a + b

def main():
  fib_sequence = fibGenerator(10)

  for num in fib_sequence:
    print(num)

if __name__ == '__main__':
  main()
