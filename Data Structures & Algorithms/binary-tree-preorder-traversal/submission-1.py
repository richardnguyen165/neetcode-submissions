# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Iterative solution
        res = []

        '''
        Call Stack Simulation
        [] (Begin, nothing called yet)
        [1] (Go Down Left)
        [1, 2] (Go Down Left)
        [1, 2, 4] (Go Down Left)
        [1, 2] (Pop out 4)
        [1, 2, 5]
        
        - The pop needs to happen right when we begin to go down the right subtree
        '''

        '''
        Stack: LIFO
        '''

        def call_stack(root):
            call_stack = []
            current_node = root

            while current_node or call_stack:
                # Wrong idea, push the right child first, since a stack is LIFO
                
                # Middle, add its value
                if current_node:
                    res.append(current_node.val)
                    call_stack.append(current_node.right)
                    current_node = current_node.left
                else:
                    current_node = call_stack.pop()
        
        call_stack(root)

        return res
        