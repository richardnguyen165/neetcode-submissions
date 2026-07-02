# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, current_sum = 0):
            if not node:
                return current_sum - 1, True
            current_total = current_sum
            left_result =  dfs(node.left, current_sum + 1)
            right_result = dfs(node.right, current_sum + 1)
            result = abs((left_result[0] - current_total) - (right_result[0] - current_total))
            result_bool = (result <= 1) and (left_result[1] and right_result[1])
            return max(left_result[0], right_result[0]), result_bool
        _, result = dfs(root)
        return result