# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        '''
        Approach 2: DFS
        Left side
        '''
        all_levels = []

        def dfs(node, depth):
            if not node:
                return None
            if len(all_levels) == depth:
                all_levels.append([])
            all_levels[depth].append(node.val)
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)
 
        res = []
        for level in all_levels:
            res.append(level[-1])

        return res
        
