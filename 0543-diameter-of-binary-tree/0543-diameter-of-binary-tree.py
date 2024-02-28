# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
  def diameterOfBinaryTree(self, root) :
    self.maxx = 0

    def maxDepth(root) :

      if not root:
        return 0

      l = maxDepth(root.left)
      r = maxDepth(root.right)
      self.maxx = max(self.maxx, l + r)
      return 1 + max(l, r)

    maxDepth(root)
    return self.maxx
        