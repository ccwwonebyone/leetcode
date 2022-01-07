# Definition for a binary tree node.
import sys


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.dps(root, sys.maxsize, -sys.maxsize - 1)

    def dps(self, root: TreeNode,  maxNum: int, minNum: int):
        if root is None:
            return True

        if root.left is not None and (root.left.val >= root.val or root.left.val <= minNum or self.dps(root.left, root.val, minNum) is False):
            return False

        if root.right is not None and (root.right.val <= root.val or root.right.val >= maxNum or self.dps(root.right, maxNum, root.val) is False):
            return False

        return True


