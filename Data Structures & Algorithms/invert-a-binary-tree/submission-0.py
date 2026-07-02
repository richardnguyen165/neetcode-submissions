# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # As per the hint, we can do this recursively -> DFS
        # Swap the nodes -> start at the bottom, move to the top
        # Stack DFS, Queue BFS

        if not root:
            return None

        '''
        root.right = self.invertTree(root.left)
        root.left = self.invertTree(root.right)

        root.right being changed already
        '''


        left_root = self.invertTree(root.left)
        right_root = self.invertTree(root.right)

        root.right = left_root
        root.left = right_root

        return root
        

