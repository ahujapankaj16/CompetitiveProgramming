'''
In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.


'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def getParentD(x,root,dep):
    if root.left is not None:
        if root.left.val == x:
            return root,dep+1
        else:
            p,q = getParentD(x,root.left,dep+1)
            if p is not None:
                return p,q
    if root.right is not None:
        if root.right.val == x:
            return root,dep+1
        else:
            p,q = getParentD(x,root.right,dep+1)
            if p is not None:
                return p,q
    return None,None
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        
        parentx, depthx = getParentD(x,root,0)
        parenty, depthy = getParentD(y,root,0)
        if depthx==depthy and parentx!=parenty:
            return True
        else:
            return False
        
        

        
