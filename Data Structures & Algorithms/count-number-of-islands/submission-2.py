class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visitation_matrix = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]

        def traverse_grid(row, col):
            visitation_matrix[row][col] = True
            if row - 1 >= 0 and grid[row - 1][col] == "1" and not visitation_matrix[row - 1][col]:
                traverse_grid(row - 1, col)
            if row + 1 <= len(grid) - 1 and grid[row + 1][col] == "1" and not visitation_matrix[row + 1][col]:
                traverse_grid(row + 1, col)
            if col - 1 >= 0 and grid[row][col - 1] == "1" and not visitation_matrix[row][col - 1]:
                traverse_grid(row, col - 1)
            if col + 1 <= len(grid[0]) - 1 and grid[row][col + 1] == "1" and not visitation_matrix[row][col + 1]:
                traverse_grid(row, col + 1)

        island_count = 0

        for row_index in range(0, len(grid)):
            for col_index in range(0, len(grid[0])):
                element = grid[row_index][col_index]
                if element == "1" and not visitation_matrix[row_index][col_index]:
                    island_count += 1
                    traverse_grid(row_index, col_index)
        
        return island_count
