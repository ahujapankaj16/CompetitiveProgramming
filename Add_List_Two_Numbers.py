# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        m=1
        sum1=0
        while l1 != None:
            sum1=sum1+m*l1.val
            m=m*10
            l1=l1.next
        print(sum1)
        m=1
        sum2=0
        while l2 != None:
            sum2=sum2+m*l2.val
            m=m*10
            l2=l2.next
        print(sum2)
        sum3=sum1+sum2
        r=sum3%10
        sum3=sum3//10
        head=temp=ListNode(r)
        while sum3 != 0:
            r=sum3%10
            sum3=sum3//10
            p=ListNode(r)
            temp.next=p
            temp=p
            
        return head
