# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        last_node = None
        if not head : 
            return None
        if not head.next :
            return head
        current = head
        while current.next.next : 
            current = current.next
        last_node = current.next 
        current.next = None 
        last_node.next = self.reverseList(head) 
        return last_node


        
        
        