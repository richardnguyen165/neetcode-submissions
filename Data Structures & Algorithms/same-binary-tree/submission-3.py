# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        '''
        Divide into sub problems:

        root node => check if they are equal
        recurse on the left
        recurse on the right

        points to consider: what if no left child or right child?
        '''
        # Current node
        if (p is not None and q is not None):
            same_node_equal = p.val == q.val
            left_node_equal = self.isSameTree(p.left, q.left)
            right_node_equal = self.isSameTree(p.right, q.right)
            return same_node_equal and left_node_equal and right_node_equal
        else:
            p_current = p.val if p is not None else None
            p_left = p.left if p is not None else None
            p_right = p.right if p is not None else None

            q_current = q.val if q is not None else None
            q_left = q.left if q is not None else None
            q_right = q.right if q is not None else None

            same_node_equal = p_current == q_current
            left_node_equal = p_left == q_left
            right_node_equal = p_right == q_right
            return same_node_equal and left_node_equal and right_node_equal