class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visitation_matrix = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

        def in_bounds(row_number, col_number):
            return 0 <= row_number < len(grid) and 0 <= col_number < len(grid[0])

        def dfs_traversal(row_number, col_number, current_area):
            visitation_matrix[row_number][col_number] = True

            ALL_DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for direction in ALL_DIRECTIONS:
                if in_bounds(row_number + direction[0], col_number + direction[1]) and not visitation_matrix[row_number + direction[0]][col_number + direction[1]] and grid[row_number + direction[0]][col_number + direction[1]] == 1:
                    current_area = max(dfs_traversal(row_number + direction[0], col_number + direction[1], current_area + 1), current_area)
            
            return current_area

        max_area = 0

        for row_number in range(len(grid)):
            for col_number in range(len(grid[0])):
                if grid[row_number][col_number] == 1 and not visitation_matrix[row_number][col_number]:
                    max_area = max(max_area, dfs_traversal(row_number, col_number, 1))
        
        return max_area