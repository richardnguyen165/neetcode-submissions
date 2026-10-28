# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        '''
        Important thing to note: A BST is a tree where all nodes on the left less than current node, all nodes on the right greater than current node
        '''

        # Try DFS

        '''
        Two cases:

        One above the other,
        It means at some point, one node would be found before the other,

        One at the same layer (harder, it means they have to be in a non-straight line)
        '''

        # At each stage, we need to know if it is split or not

        # Case 1: All going to the left (strictly all lower)
        if p.val < root.val and q.val < root.val and root.left:
            return self.lowestCommonAncestor(root.left, p, q)
        # Case 2: All going to the right (strictly all greater)
        elif p.val > root.val and q.val > root.val and root.right:
            return self.lowestCommonAncestor(root.right, p, q)
        # It either splits, or at least one of them are equal to the root
        elif p.val == root.val:
            return p
        elif q.val == root.val:
            return q
        else:
            return root

