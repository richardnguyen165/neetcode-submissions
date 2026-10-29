# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root:
            current_queue = deque([root])
            final_tree = [[root.val]]
        else:
            return []

        next_level = deque([])

        final_tree = []
        current_level = []

        while current_queue:
            current_node = current_queue.popleft()
            current_level.append(current_node.val)

            if current_node.left:
                next_level.append(current_node.left)
            if current_node.right:
                next_level.append(current_node.right)
            
            if not current_queue:
                final_tree.append(current_level)
                current_queue = next_level
                next_level = deque([])
                current_level = []
            
        return final_tree