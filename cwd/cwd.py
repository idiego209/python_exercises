import os

def getInode(filename):
  """
  Helper function.
  Arguments:
    String: filename
  Returns:
    int: s.st_ino Inode number.   int: s.st_dev Device number.
  """
  s = os.stat(filename)
  return s.st_ino, s.st_dev

def getFileName(target_ino, target_dev, parent_dir):
  """
  Check all filenames until we have a match.
  Arguments:
    string: filename_to_match
      Filename within parent directory we are looking for.
    string: parent_dir
      Name of the parent directory we are looking in.
  Returns:
    List: [filename] Filename match.
  """
  for filename in os.listdir(parent_dir):
    # Skip files only interested in directories.
    # Use lstat to follow ism links.
    s = os.lstat(os.path.join(parent_dir, filename))
    if not os.path.stat.S_ISDIR(s.st_mode):
      continue
    try:
      filename_ino, filename_dev = getInode(os.path.join(parent_dir, filename, '.'))
      if filename_ino == target_ino and filename_dev == target_dev:
        return [filename]
    # Catch permission errors
    except OSError, e:
      continue

def getAbsPath(root_ino, root_dev, filename):
  """
  Return current working directory.
  Arguments:
    int: root_ino Inode number of root.
    int: root_dev device number of root.
    string: Filename name of working directory.
  Returns:
    list: path List contining absolute path.
  """
  # Get inode info for working directory.
  filename_ino, filename_dev = getInode(filename)
  # Check if cwd is the root dir.
  if root_ino == filename_ino and root_dev == filename_dev:
    return ['/']
  # Get path of parent directory.
  parent_dir = os.path.join(filename, '..')
  path = getAbsPath(root_ino, root_dev, parent_dir)
  return path + getFileName(filename_ino, filename_dev, parent_dir)

def main():
  root_ino, root_dev = getInode('/')
  abs_path = getAbsPath(root_ino, root_dev, '.')
  print(os.path.join(*abs_path))

if __name__ == '__main__':
  main()
