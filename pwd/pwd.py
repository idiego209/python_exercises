import os

def getInode(filename):
  inode_num, dev_id = os.stat(filename)
  return ino, dev_id

def getFileName(filename_to_match, parent_dir):
# for filename in os.listdir(parent_dir)
# skip files only interested in filenames
# if file skip
# getInode
# if inode of filename == filename_to_match
# return filename
# else go to next filename
  for filename in os.listdir(parent_dir):

def getAbsPath(filename, root):
# function parameters pwd (.)
# helper function to get inode # getInode
# check if . ino == roo_ino return [/]
# else recursive call to self getAbsPath('/..', root_ino)
# path = helper function traverse filenames find /.. parent dir /../. dir to match
# return [path]
  inode_num, dev_id = getInode(filename)
  root_inode_num, root_dev_id = getInode(root)

  if root_inode_num == inode_num:
    return ['/']
  parent_dir = '../.'
  path = getAbsPath(parent_dir, root)
  path.append(getFileName, parent_dir)
  retun path

def main():
  abs_path = getAbsPath('.', '/')

if __name__ == '__main__':
  main()
