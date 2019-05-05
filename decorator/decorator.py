#!/usr/bin/env python
# decorator.py
# Example use of decorators.
# Decorator function calculates time of completion.
# Author: https://github.com/idiego209
import time

def time_func(func):
  def wrapper(*args, **kwargs):
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    # Time in milliseconds
    enlapsed_time =(end_time - start_time) * 1000
    print("{} took {} mil secs to run.").format(func.__name__, enlapsed_time)
    return result
  return wrapper

@time_func
def calc_square(nums):
  result = []
  for num in nums:
    result.append(num * num)
  return result

@time_func
def calc_cube(nums):
  result = []
  for num in nums:
    result.append(num * num * num)
  return result

@time_func
def calc_square_generator(nums):
  return (x*x for num in nums)

@time_func
def calc_cube_generator(nums):
  return (x*x*x for num in nums)

def main():
  array = range(1,100000)
  calc_square(array)
  calc_cube(array)
  calc_square_generator(array)
  calc_cube_generator(array)

if __name__ == '__main__':
  main()
