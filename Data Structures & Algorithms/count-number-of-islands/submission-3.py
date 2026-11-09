class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visitation_matrix = [[False for  _ in range(len(grid[0]))] for _ in range(len(grid))]
        
        def within_bounds(row_index, col_index):
            return (0 <= row_index <= (len(grid) - 1)) and (0 <= col_index <= (len(grid[0]) - 1))
        
        def traverse_island(row_index, col_index):
            visitation_matrix[row_index][col_index] = True

            if within_bounds(row_index + 1, col_index) and not visitation_matrix[row_index + 1][col_index] and grid[row_index + 1][col_index] == "1":
                traverse_island(row_index + 1, col_index)
            if within_bounds(row_index - 1, col_index) and not visitation_matrix[row_index - 1][col_index] and grid[row_index - 1][col_index] == "1":
                traverse_island(row_index - 1, col_index)
            if within_bounds(row_index, col_index + 1) and not visitation_matrix[row_index][col_index + 1] and grid[row_index][col_index + 1] == "1":
                traverse_island(row_index, col_index + 1)
            if within_bounds(row_index, col_index - 1) and not visitation_matrix[row_index][col_index - 1] and grid[row_index][col_index - 1] == "1":
                traverse_island(row_index, col_index - 1)

        island_count = 0

        for row_index in range(0, len(grid)):
            for col_index in range(0, len(grid[0])):
                if grid[row_index][col_index] == "1" and not visitation_matrix[row_index][col_index] :
                    island_count += 1
                    traverse_island(row_index, col_index)

        return island_count