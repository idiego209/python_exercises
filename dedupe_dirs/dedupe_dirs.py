#!/usr/bin/env python
# dedupe_dirs.py
# Given two directories dedupe contents.
# Author: https://github.com/idiego209

import os
import hashlib

def getFileSize(file):
  s = os.stat(file)
  return s.st_size

def hashContent(content):
  new_hash = hashlib.md5()
  new_hash.update(content)
  new_hash_digest = new_hash.digest()
  return new_hash_digest

def getContent(filename):
  with open(filename, 'r') as f:
    content = f.read()
  return content

def duplicate(file1, file2):
  """
  Checks if file1 is duplicate of file2
  Arguments:
    string: file1, file2 files to check.
  Returns:
    boolean: True if duplicate else False
  """
  file1_content = getContent(file1)
  file2_content = getContent(file2)
  file1_hash = hashContent(file1_content)
  file2_hash = hashContent(file2_content)

  return file1_hash == file2_hash

def getDuplicates(directories):
  """
  Checks for duplicates in directories.
  Arguments:
    list: directories Directories to check for duplicates
  Returns:
    list: duplicates Files that are duplicates.
  """
  file_size_dic = {}
  files_to_delete = []

  for dir in directories:
    for file in os.listdir(dir):
      file_size = getFileSize(os.path.join(dir, file))
      if file_size not in file_size_dic:
        file_size_dic[file_size] = os.path.join(dir, file)
      else:
        file2 = file_size_dic[file_size]
        if duplicate(os.path.join(dir, file), file2):
          files_to_delete.append(os.path.join(dir, file))
  return files_to_delete

def dedupe(directories):
  """
  Delete duplicate files.
  Arguments:
    list: directories List containing dirs to dedupe
  """
  files_to_delete = []

  files_to_delete = getDuplicates(directories)
  for file in files_to_delete:
    print("Duplicate file removed: {}").format(file)
    os.remove(file)

def main():
  dir1 = os.path.join(os.getcwd(), 'test_data/dir1')
  dir2 = os.path.join(os.getcwd(), 'test_data/dir2')

  directories = []
  directories.append(dir1)
  directories.append(dir2)
  dedupe(directories)

if __name__ == '__main__':
  main()
