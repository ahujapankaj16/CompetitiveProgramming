'''
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
'''
import sys
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head=s=ListNode(sys.maxsize)
        tempval=sys.maxsize
        templ=-1
        while True:
            for i in range(len(lists)):
                if lists[i] is not None:
                    if tempval > lists[i].val:
                        tempval=lists[i].val
                        templ=i
            if templ == -1:
                break
            p=ListNode(tempval)
            s.next=p
            s=p
            lists[templ]=lists[templ].next
            tempval=sys.maxsize
            templ=-1
        return head.next
