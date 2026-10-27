# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Conduct dfs in in-order traversal
    def dfs(self, root: Optional[TreeNode]):
        if root is None:
            return []
        return self.dfs(root.left) + [root.val] + self.dfs(root.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        # Step 1: Create the DFS iteration of the subroot
        sub_root_tree_dfs = self.dfs(subRoot)

        home_node = root

        if root is None:
            return sub_root_tree_dfs == root
        else:
            # Step 2: Iterate through the root, each child returns back
            # above
            def modified_dfs(root):
                if root is None:
                    return (root == subRoot, [])
                left_result = modified_dfs(root.left)
                right_result = modified_dfs(root.right)
                result_tree = left_result[1] + [root.val] + right_result[1]
                result_prev = left_result[0] or right_result[0] or result_tree == sub_root_tree_dfs
                return (result_prev, result_tree)
            return modified_dfs(root)[0]
            
            