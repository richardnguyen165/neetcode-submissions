"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        '''
        New approach: First iteration, copy all the nodes

        But how do we deal with the random nodes?

        Okay, 

        Create a hashmap consisting of:

        Key: old node
        Value: new node

        Create a second hashmap responsible for point to the random consisting of:

        Key: old node
        Value: old random node

        Then we iterate through the second hashmap, and find the old node's old random node's new node, and connect random node
        '''

        new_head = None # we return this

        old_to_new = {}
        old_random = {}
        prev_node_first = None

        while head:
            new_node = Node(head.val)

            # Clone the old node
            old_to_new[head] = new_node
            # Map the old node to it's random node
            old_random[head] = head.random

            if not new_head:
                # Initializing the new node
                new_head = new_node
            if not prev_node_first:
                prev_node_first = new_node
            # Set the previous node next value to this new node
            # Then move to the new node
            else:
                prev_node_first.next = new_node
                prev_node_first = new_node
            head = head.next

        # Now go thorugh the random nodes
        for old_node, old_random_node in old_random.items():

            if old_random_node:
                # Get the new node 
                new_node = old_to_new[old_node]
                new_node.random = old_to_new[old_random_node]


        return new_head