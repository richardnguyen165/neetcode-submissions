# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import math

class Solution:
    '''
    New flaw:

    What if there is a greater node in the left subtree?
    We need to pass back the max and the min values

    Return values (lowest value, highest value, bool)
    '''
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs_modified(root):
            if not root:
                return (math.inf, -math.inf, True)
                
            current_node_check = True
            if root.right:
                current_node_check = current_node_check and (root.right.val > root.val)
            if root.left:
                current_node_check = current_node_check and (root.left.val < root.val)
            
            left_result = dfs_modified(root.left)
            right_result = dfs_modified(root.right)

            # Check left
            left_check = True
            if root.left:
                # What we are doing here is checking if our current node value is always greater than the maximum value in the left subtree, if so, means all values are greater than all values in the left subtree
                left_check = root.val > left_result[1] and left_result[2]       

            # Check right
            right_check = True
            if root.right:
                # What we are doing is checking if our current node valiue is always less than the minimum value in the right subtree, if so, means that it is less than all the values in the right subtree
                right_check = root.val < right_result[0] and right_result[2]
            
            # return left + current + right
            return (min(root.val, left_result[0], right_result[0]), max(root.val, left_result[1], right_result[1]), left_check and right_check and current_node_check)

        return dfs_modified(root)[2]