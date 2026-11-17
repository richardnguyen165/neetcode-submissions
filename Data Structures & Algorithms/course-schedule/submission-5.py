class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Cycle detection problem

        # Step 1:
        # Connect the graph

        all_nodes = {}

        # Initialize a neighbor matrix
        for c_n in range(numCourses):
            all_nodes[c_n] = set()

        # Go through prereqsiquites
        for p in prerequisites:
            all_nodes[p[0]].add(p[1]) # Go from its preresqiuites 

        # Using the all_nodes as an adjacency matrix, find all the neighbors
        # If we land back on a node we visited return false, else return true

        # Step 2: Cycle detection

        # How can we consider disconnected nodes?
        # Conduct a BFS at each node? TLE
        # What about considering sub-graphs: if that node already has been visited, it means it subgraph has been visited
        # Right answer: DFS

        # Ok, add a set where any cleared node that has no cycle

        # Looking at neetcode solution

        all_visited = set()

        def visited_nodes(node_number):
            if node_number in all_visited:
                return False # It means a cycle is decteted in the current DFS iteration
            if len(all_nodes[node_number]) == 0:
                return True # It means that all that node AND ITS DESCENDANTS is not in a cycle
            
            # Indicate that we have visited 
            all_visited.add(node_number)
            for neighbor in all_nodes[node_number]:
                if not visited_nodes(neighbor): # That descendant has a cycle
                    return False
            # We reach this point, no cycle
            all_visited.remove(node_number) # Remove for next iteration
            all_nodes[node_number] = set()
            return True
        
        result = True
        for n in range(numCourses):
            result = result and visited_nodes(n)

        return result