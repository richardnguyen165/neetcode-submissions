from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        '''
        We go level by level (BFS)
        '''
        if not p and not q:
            return True
        elif (not p and q) or (not q and p):
            return False

        p_node_current = [p]
        q_node_current = [q]

        p_node_val = [p.val]
        q_node_val = [q.val]

        print()

        while (p_node_current and q_node_current):
            if p_node_val != q_node_val:
                return False

            # Empty out old values
            p_node_val = []
            q_node_val = []

            p_node_past = p_node_current
            q_node_past = q_node_current

            # Empty out old nodes, to clear way for the next nodes
            p_node_current = []
            q_node_current = []

            for node in p_node_past:
                if node:
                    p_node_current.append(node.left)
                    p_node_current.append(node.right)
                    if node.left:
                        p_node_val.append(node.left.val)
                    else:
                        p_node_val.append(None)
                    if node.right:
                        p_node_val.append(node.right.val)
                    else:
                        p_node_val.append(None)
            
            for node in q_node_past:
                if node:
                    q_node_current.append(node.left)
                    q_node_current.append(node.right)
                    if node.left:
                        q_node_val.append(node.left.val)
                    else:
                        q_node_val.append(None)
                    if node.right:
                        q_node_val.append(node.right.val)
                    else:
                        q_node_val.append(None)

        return True 
