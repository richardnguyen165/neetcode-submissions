import math

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # Multi source bfs
        # Start from all treasure chests at once

        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def in_bounds(r, c):
            return (0 <= r < len(grid)) and (0 <= c < len(grid[0]))

        def multi_bfs(starting_deque):

            next_deque = deque()
            current_level = 1

            while starting_deque:
                current_node = starting_deque.popleft()

                for direction in DIRECTIONS:
                    r_inc = direction[0]
                    c_inc = direction[1]
                    if (in_bounds(current_node[0] + r_inc, current_node[1] + c_inc) and grid[current_node[0] + r_inc][current_node[1] + c_inc] == 2147483647):
                        grid[current_node[0] + r_inc][current_node[1] + c_inc] = current_level
                        next_deque.append([current_node[0] + r_inc, current_node[1] + c_inc])

                if not starting_deque and next_deque:
                    current_level += 1
                    starting_deque.extend(next_deque)
                    next_deque = deque()

        bfs_deque = deque()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    bfs_deque.append([r, c])
        
        multi_bfs(bfs_deque)
