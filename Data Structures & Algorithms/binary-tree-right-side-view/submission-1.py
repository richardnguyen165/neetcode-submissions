# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        '''
        Approach 1: BFS
        '''

        if not root:
            return []

        q = deque([root])
        all_levels = []


        while q:
            length_of_q = len(q)
            current_level = []

            for _ in range(length_of_q):
                node = q.popleft()
                if node:
                    current_level.append(node.val)
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            
            all_levels.append(current_level)

        right_side = []
        for level in all_levels:
            right_side.append(level[-1])
        
        return right_side


        
