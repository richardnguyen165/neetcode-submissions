# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Non recursive DFS
        res = 0
        def dfs(node):
            nonlocal res
            
            if not node: 
                return 0
            left_result = dfs(node.left)
            right_result = dfs(node.right)
            res = max(left_result + right_result, res)
            return max(left_result, right_result) + 1
        dfs(root)
        return res
        
