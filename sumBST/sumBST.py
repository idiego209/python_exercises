#!/usr/bin/env python
# https://leetcode.com/problems/range-sum-of-bst/
# sumBST.py
# Given the root node of a binary search tree, return the sum
# of values of all nodes with value between L and R (inclusive).
# The binary search tree is guaranteed to have unique values.
# Author: https://github.com/idiego209
def sumBST(node):
            if node:
                if L <= node.val <= R:
                    self.sum += node.val
                if L < node.val:
                    sumBST(node.left)
                if R > node.val:
                    sumBST(node.right)
        self.sum = 0
        sumBST(root)
        return self.sum
