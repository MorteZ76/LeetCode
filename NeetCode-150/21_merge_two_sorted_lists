
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged_list = ListNode()
        if not (list1 or list2) :
            return None
        current = merged_list
        while list1 or list2:
            number1 = 102
            number2 = 102
            if list1  : 
                number1 = list1.val
            if list2  : 
                number2 = list2.val
            if number1 <= number2 :
                current.val = number1
                list1 = list1.next
            else :
                current.val = number2
                list2 = list2.next
            if list1 or list2: 
                current.next = ListNode()
                current = current.next
            
        
        return merged_list
            


        