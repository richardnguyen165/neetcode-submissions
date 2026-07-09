# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Solution 2: call stack
        res = []

        def call_stack(root):
            call_stack = []

            # Initalize with the root and current as pointer
            current = root

            # Keep recursing until the call stack is empty
            while current or call_stack:
                # Go left (keepp going left until you can't)
                while current:
                    call_stack.append(current)
                    current = current.left

                # Middle (add the node's current value)
                current = call_stack.pop()
                res.append(current.val)

                # Go right
                current = current.right
        
        call_stack(root)

        return res