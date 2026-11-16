from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Multisource BFS?
        # Find all cells that can flow to atlantic => add to set
        # Find all cells that can flow to pacific =>  add to set
        # Find the intersection of both sets

        bfs_stack = deque()

        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def in_bounds(r, c):
            return (0 <= r < len(heights)) and (0 <= c < len(heights[0]))

        def bfs_traversal(starting_deque):
            reachable_set = set()

            # Add starting points to set
            for point in starting_deque:
                reachable_set.add(point)

            while starting_deque:
                cr = starting_deque.popleft()
                for d in DIRECTIONS:
                    r_inc = d[0]
                    c_inc = d[1]
                    if (in_bounds(cr[0] + r_inc, cr[1] + c_inc)) and ((cr[0] + r_inc, cr[1] + c_inc) not in reachable_set) and heights[cr[0] + r_inc][cr[1] + c_inc] >= heights[cr[0]][cr[1]]:
                        reachable_set.add((cr[0] + r_inc, cr[1] + c_inc))
                        starting_deque.append((cr[0] + r_inc, cr[1] + c_inc))
            
            return reachable_set

        # Step 1: Find pacific

        # First, add all the cells on the left side

        for r in range(len(heights)):
            bfs_stack.append((r, 0))

        # Second, add all the cells on the top side
        for c in range(len(heights[0])):
            bfs_stack.append((0, c))

        # Then conduct bfs on it to find all the cells that can reach it
        pacific_result = bfs_traversal(bfs_stack)

        # Step 2: Find atlantic

        # First, add all the cells on the right side

        bfs_stack = deque()

        for r in range(len(heights)):
            bfs_stack.append((r, len(heights[0]) - 1))

        # Second, add all the cells on the top side
        for c in range(len(heights[0])):
            bfs_stack.append((len(heights) - 1, c))

        atlantic_result = bfs_traversal(bfs_stack)

        both_flows = atlantic_result.intersection(pacific_result)

        return list(both_flows)

