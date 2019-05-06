#!/usr/bin/env python
# keyword_count.py
# Find keyword and return number of entries in document.
# Author: https://github.com/idiego209
import os

def countLines(file_path, keyword):
  """
  Keeps count of number of times keyword is found in document.
  Arguments:
    string: file_path Absolute file path of document to be checked.
    string: keyword Keyword we are looking for within document.
  Returns:
    int: count Number of times keyword was found in document.
  """
  count = 0

  try:
    with open(file_path, 'r') as f:
      lines = f.readlines()
      if keyword in lines:
        count += 1
  # Catch permission errors.
  except OSError as e:
    print("{}. Could not open file {}.").format(e, file_path)
  return count

def getKeywordCount(cwd, keyword):
  """
  Find number of time keyword is found across all documents in
  current working directory.
  Arguments:
    string: cwd Current working directory.
    string: keyword Keyword we are looking for.
  Returns:
    int: lines_count Total count of keyword across all docs checked.
  """
  lines_count = 0

  for dirpath, dirnames, filenames in os.walk(cwd):
    for file in filenames:
      file_path = os.path.join(dirpath, file)
      lines_count += countLines(file_path, keyword)
  return lines_count

def main():
  cwd = os.getcwd()
  keyword = 'palindrome'

  total_lines = getKeywordCount(cwd, keyword)
  print(total_lines)

if __name__ == '__main__':
  main()
