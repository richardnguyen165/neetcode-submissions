from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Multi source BFS

        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def in_bounds(r, c):
            return (0 <= r < len(grid)) and (0 <= c < len(grid[0]))

        def bfs_traversal(starting_stack):
            
            next_level = deque()
            current_level = 0

            while starting_stack:
                current_fruit = starting_stack.popleft()
                for direction in DIRECTIONS:
                    row_inc = direction[0]
                    col_inc = direction[1]
                    if in_bounds(current_fruit[0] + row_inc, current_fruit[1] + col_inc) and grid[current_fruit[0] + row_inc][current_fruit[1] + col_inc] == 1:
                        grid[current_fruit[0] + row_inc][current_fruit[1] + col_inc] = 2
                        next_level.append([current_fruit[0] + row_inc, current_fruit[1] + col_inc])
                
                if not starting_stack and next_level:
                    current_level += 1
                    starting_stack.extend(next_level)
                    next_level = deque()
            
            return current_level

        bfs_stack = deque()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 2:
                    bfs_stack.append([r, c])
       
        result = bfs_traversal(bfs_stack)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    return -1
        
        return result
