'''

Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \     
      4   5    
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].

Note: The length of path between two nodes is represented by the number of edges between them.


'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        
        mx=0
        if root is None:
            return 0
        def calculateD(root):
            nonlocal mx
            lf=rf=0
            if root.left is None and root.right is None:
                return 1
            if root.left is not None:
                lf= calculateD(root.left)
            if root.right is not None:
                rf = calculateD(root.right)
            
            mx = max(mx,lf+rf)
            
            return (1+max(lf,rf))
        
        ans = calculateD(root)
        return mx
            
        
