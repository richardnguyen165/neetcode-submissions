from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # BFS
        visitation_matrix = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

        def in_bounds(row_number, col_number):
            return 0 <= row_number < len(grid) and 0 <= col_number < len(grid[0])

        def bfs_traversal(row_number, col_number):
            bfs_stack = deque()
            bfs_stack.append([row_number, col_number])
            visitation_matrix[row_number][col_number] = True
            area_count = 0
            ALL_DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            while len(bfs_stack) > 0 :
                current_node = bfs_stack.popleft()

                area_count += 1
                for direction in ALL_DIRECTIONS:
                    if in_bounds(current_node[0] + direction[0], current_node[1] + direction[1]) and not visitation_matrix[current_node[0] + direction[0]][current_node[1] + direction[1]] and grid[current_node[0] + direction[0]][current_node[1] + direction[1]] == 1:
                        bfs_stack.append([current_node[0] + direction[0], current_node[1] + direction[1]])
                        visitation_matrix[current_node[0] + direction[0]][current_node[1] + direction[1]] = True

            return area_count
        
        max_area = 0

        for row_number in range(len(grid)):
            for col_number in range(len(grid[0])):
                if grid[row_number][col_number] == 1 and not visitation_matrix[row_number][col_number]:
                    max_area = max(max_area, bfs_traversal(row_number, col_number))
        
        return max_area