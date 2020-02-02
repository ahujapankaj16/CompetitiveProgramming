####Problem: Given a binary tree, return the sum of values of its deepest leaves.

####Solution


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findMaxDepth(self,root: TreeNode):
        if root==None:
            return 0
        left=self.findMaxDepth(root.left)
        right=self.findMaxDepth(root.right)
        return max(left,right)+1
    def deepestLeavesSum(self, root: TreeNode) -> int:

        n=self.findMaxDepth(root)
        
        result=self.inorderTraversal(root,n)
        return result
    
    def inorderTraversal(self,root,n):
        if root==None:
            return 0
        if n==1 and root.left==None and root.right== None:
            return root.val
        
        suml=self.inorderTraversal(root.left,n-1)
        sumr=self.inorderTraversal(root.right,n-1)
        return suml+sumr

def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root

def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            root = stringToTreeNode(line);
            
            ret = Solution().deepestLeavesSum(root)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()