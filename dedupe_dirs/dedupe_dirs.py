#!/usr/bin/env python
# dedupe_dirs.py
# Given two directories dedupe contents.
# Author: https://github.com/idiego209

import os
import hashlib

def getFileSize(file):
  """
  Arguments:
    string: file Filename to be checked.
  Returns:
    int: s.st_size File size in bytes.
  """
  s = os.stat(file)
  return s.st_size

def hashData(filename):
  """
  Hashes filename contents.
  Arguments:
    string: filename Filename to be hashed.
  Returns:
    string: hash.digest() Hash digest.
  """
  hash = hashlib.md5()
  file_data = getContent(filename)
  hash.update(file_data)
  return hash.digest()

def getContent(filename):
  with open(filename, 'r') as f:
    file_data = f.read()
  return file_data

def getDuplicates(directories):
  """
  Checks for duplicates in directories.
  Arguments:
    list: directories Directories to check for duplicates
  Returns:
    list: duplicates Files that are duplicates.
  """
  size = {}
  hash_data = {}
  files_to_delete = []

  for dir in directories:
    for file in os.listdir(dir):
      file_size = getFileSize(os.path.join(dir, file))
      if file_size not in size:
        size[file_size] = os.path.join(dir, file)
        continue
      file1_hash = hashData(os.path.join(dir, file))
      if file1_hash in hash_data:
        files_to_delete.append(os.path.join(dir, file))
        continue
      file2_hash = hashData(size[file_size])
      if file1_hash == file2_hash:
        hash_data[file1_hash] = os.path.join(dir, file)
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
