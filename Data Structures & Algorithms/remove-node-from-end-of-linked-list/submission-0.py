# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = head

        slow = head
        fast = head

        current_n  = 1

        while (current_n != n):
            fast = fast.next
            current_n += 1
        
        previous = None
        while (fast.next != None):
            previous = slow
            slow = slow.next
            fast = fast.next
        
        # remove phase

        if previous == None:
            # move to the next node (your removing only the first node)
            dummy = head.next

        # first node at the end of the list
        elif slow.next == None:
            previous.next = None
        
        # in the middle, both previous and end node exists
        else:
            previous.next = slow.next

        return dummy