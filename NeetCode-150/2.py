# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        out = l1
        parent = None
        while l1:
            l1_num = l1.val
            l2_num = 0
            if l2 :
                l2_num = l2.val
                l2 = l2.next
            if l1_num + l2_num > 9 :
                l1.val = l1_num + l2_num -10
                if l1.next : 
                    l1.next.val += 1
                else :
                    l1.next = ListNode(1)
            else :
                l1.val = l1_num + l2_num 

            parent = l1
            l1 = l1.next
                
        if l2 :
            parent.next = l2
            l1 = l2
            
        return out 

            
        