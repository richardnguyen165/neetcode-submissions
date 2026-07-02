# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1
        
        list1_val = list1.val
        list2_val = list2.val
        print(list1_val, list2_val)

        if list1_val <= list2_val:
            current_node = list1
            current_node.next = self.mergeTwoLists(list1.next, list2)
            return current_node
        else:
            current_node = list2
            current_node.next = self.mergeTwoLists(list1, list2.next)
            return current_node