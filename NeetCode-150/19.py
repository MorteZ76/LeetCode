# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        real_head = head
        parents = []
        if not head.next :
            return None
        while head.next :
            parents.append(head)
            head = head.next
        if n == len(parents) + 1:
            return parents[0].next
        if n == 1 :
            parents[-1].next = None
            return real_head
        del_node_parent = parents[len(parents)-n + 1]
        parents[len(parents)-n].next = del_node_parent.next
        return real_head
        

        

        