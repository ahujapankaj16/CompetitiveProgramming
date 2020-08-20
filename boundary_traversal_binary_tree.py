#User function Template for python3


'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
# your task is to complete this function
# function should return a list containing the boundary view of the binary tree
def printBoundaryView(root):
    # Code here
    
    que = []
    def inorder(root):
        if root is None:
            return
        inorder(root.left)
        if root.left is None and root.right is None:
            que.append(root.data)
        inorder(root.right)
    que.append(root.data)
    #print left
    
    ptr = root.left
    while ptr is not None:
        if ptr.left is None :
            if ptr.right is None:
                break
            else:
                que.append(ptr.data)
                ptr = ptr.right
        else:
            que.append(ptr.data)
            ptr = ptr.left
        
    #inorder
    inorder(root.left)
    inorder(root.right)
    ptr = root.right
    temp = []
    while ptr is not None:
        if ptr.right is None:
            if ptr.left is None:
                break
            else:
                temp.append(ptr.data)
                ptr = ptr.left
        else:
            temp.append(ptr.data)
            ptr = ptr.right
    que = que+temp[::-1]
    return que
