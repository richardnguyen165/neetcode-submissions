# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (not head):
            return head
        tail = None

        while (head):
            current_node = head
            # Very close, forgot to store the next head, which you can do
            next_head = head.next
            old_tail = tail

            current_node.next = old_tail
            tail = current_node

            head = next_head
            
        return tail