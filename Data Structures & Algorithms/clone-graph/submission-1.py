from collections import deque
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        '''
        Use a hashtable

        Where the key is node.val

        and the value is the node itself?

        but we have to traverse the node given, and return one node 

        Assumption: all nodes are connected
        '''

        if not node:
            return None

        # BFS implementation, easier

        # Start with the node given
        bfs_stack = deque()
        bfs_stack.append(node)
        all_nodes = {}
        all_nodes[node.val] = Node(node.val, [])

        while bfs_stack:
            current_node = bfs_stack.popleft()

            all_neighbor_nodes = []

            # Ok, in this step, add all of its neighbors
            for neighbor in current_node.neighbors:
                if neighbor.val not in all_nodes:
                    # FOR NEW GRAPH
                    neighbor_node = Node(neighbor.val, [])
                    # all_nodes[current_node.val] = neighbor_node (accidental override)
                    all_nodes[neighbor_node.val] = neighbor_node # correct idea
                    all_neighbor_nodes.append(neighbor_node)
                    # FOR NEW GRAPH 

                    # FOR OLD GRAPH TRAVERSAL
                    bfs_stack.append(neighbor)
                    # FOR OLD GRAPH TRAVERSAL
                else:
                    # Failed to consider this case
                    # It means it is a case where that neighbor has already been traversed already, 
                    # meaning it is the case where you need to add the other side to this node, since a connection is two ways
                    all_neighbor_nodes.append(all_nodes[neighbor.val])
            
            if all_neighbor_nodes:
                # Now append to the new graph/hashmap of node we are focusing on
                all_nodes[current_node.val].neighbors.extend(all_neighbor_nodes)

        return all_nodes[node.val]


