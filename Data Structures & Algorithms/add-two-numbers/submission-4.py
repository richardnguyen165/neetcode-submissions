# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        elif not l2:
            return l1
        
        result = None
        final_result = None

        carry_over = 0
    
        print("hi")

        while (l1):
            # if l2 is a shorter number than l1
            if l2:
                total = l1.val + l2.val + carry_over
                l2 = l2.next
            else:
                total = l1.val + carry_over

            carry_over = 0

            if total >= 10:
                total %= 10
                carry_over = 1

            total_node = ListNode(total)
            if not result:
                result = total_node
                final_result = result
            else:
                result.next = total_node
                result = result.next

            l1 = l1.next
        
        print(final_result)
        
        # if l2 is a longer number than l1
        while (l2):
            total = l2.val + carry_over
            carry_over = 0

            if total >= 10:
                total %= 10
                carry_over = 1 
            
            total_node = ListNode(total)
            result.next = total_node
            result = result.next

            l2 = l2.next
        
        if carry_over:
            total_node = ListNode(1)
            result.next = total_node
            result = result.next

        return final_result
                