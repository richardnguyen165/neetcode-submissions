# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node, current_max = 0):
            if not node:
                return current_max
            return max(dfs(node.right, current_max + 1), dfs(node.left, current_max + 1))
        return dfs(root)


