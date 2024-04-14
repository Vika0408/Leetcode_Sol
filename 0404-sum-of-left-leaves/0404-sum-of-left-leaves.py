# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        if not root :
            return 0
        
        ans = 0
        
        if root.left :
            if not root.left.left and not root.left.right:
                ans += root.left.val
            else:
                ans += self.sumOfLeftLeaves(root.left)
        ans += self.sumOfLeftLeaves(root.right)
            
        return ans
        
        """
        :type root: TreeNode
        :rtype: int
        """
        