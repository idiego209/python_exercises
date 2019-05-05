import os

def getInode(filename):
""" Helper function.
  Arguments:
    String: filename
  Returns:
    int: s.st_ino Inode number.
    int: s.st_dev Device number.
"""
  s = os.stat(filename)
  return s.st_ino, s.st_dev

def getFileName(filename_to_match, parent_dir):
""" Check all filenames until we have a match.
  Arguments:
    string: filename_to_match
      Filename within parent directory we are looking for.
    string: parent_dir
      Name of the parent directory we are looking in.
"""
  for filename in os.listdir(parent_dir):

def getAbsPath(root_ino, root_dev, filename):
""" Return current working directory.
  Arguments:
    int: root_ino Inode number of root.
    int: root_dev device number of root.
    string: Filename name of working directory.
  Returns:
    list: path List contining absolute path.
"""
  filename_ino, filename_dev = getInode(filename)

  if root_ino == filename_ino and root_dev == filename_dev
    return ['/']
  parent_dir = os.path.join('../', filename)
  path = getAbsPath(root_ino, root_dev, parent_dir)
  return path + getFileName(filename, parent_dir)

def main():
  root_ino, root_dev = getInode('/')
  abs_path = getAbsPath(root_ino, root_dev, '.')
  print(*abs_path)

if __name__ == '__main__':
  main()
