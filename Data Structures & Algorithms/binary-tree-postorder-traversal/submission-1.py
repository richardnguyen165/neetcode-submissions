# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Iterative solution
        '''
        Idea: 
        Go as left as much as possible, while adding the node to the stack, so that we can go right
        
        Then once you can no longer go left, you will need to go right

        Then append the value once left and right is done
        '''
        res = []

        def call_stack(root):
            stack = []
            cur = root

            while cur or stack:

                # Go left
                while cur:
                    # False => signifies the right subtree has not been visited
                    stack.append([cur, False])
                    cur = cur.left
                
                # You need to know what direction you came from
                # When going back to the middle node

                # Get the middle node
                current_middle_node = stack[-1]

                if current_middle_node[1]:
                    # Append the val of the current node
                    res.append(current_middle_node[0].val)
                    stack.pop()
                else:
                    cur = current_middle_node[0].right
                    # Signifies right side is being visited
                    stack[-1][1] = True
        
        call_stack(root)

        return res

