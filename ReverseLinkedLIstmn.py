# Definition for singly-linked list.

'''
Reverse a linked list from position m to n. Do it in one-pass.
Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
'''
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        p=head
        counter=1
        m1=head
        if m>=n:
            return head
        while True:
            print(p.val)
            if counter<m:
                if counter==(m-1):
                    m1=p
                p=p.next
            if counter==m:
                mo=p
                q=p
                p=p.next
                r=p.next
            if counter>m and counter<=n:
                p.next=q
                q=p
                p=r
                if r!=None:
                    r=r.next
            if counter==n:
                m1.next=q
                mo.next=p
                break
            counter=counter+1
        if m==1:
            return q
        else:
            return head
            
                