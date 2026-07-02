from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        for grids in grid:
            print(grids)

        def matrix_bfs(row, col):
            current_size = 0
            all_cords = deque()
            all_cords.append([row, col])
            while all_cords:
                popped_cord = all_cords.popleft()
                row_cord = popped_cord[0]
                col_cord = popped_cord[1]
                if not visitation_matrix[row_cord][col_cord]:
                    current_size += 1
                    visitation_matrix[row_cord][col_cord] = True
                    if row_cord - 1 >= 0 and not visitation_matrix[row_cord - 1][col_cord] and grid[row_cord - 1][col_cord]:
                        all_cords.append([row_cord - 1, col_cord])
                    if row_cord + 1 <= len(grid) - 1 and not visitation_matrix[row_cord + 1][col_cord] and grid[row_cord + 1][col_cord]:
                        all_cords.append([row_cord + 1, col_cord])
                    if col_cord - 1 >= 0 and not visitation_matrix[row_cord][col_cord - 1] and grid[row_cord][col_cord - 1]:
                        all_cords.append([row_cord, col_cord - 1])
                    if col_cord + 1 <= len(grid[0]) - 1 and not visitation_matrix[row_cord][col_cord + 1] and grid[row_cord][col_cord + 1]:
                        all_cords.append([row_cord, col_cord + 1])
            return current_size



        # Use BFS -> queue data structure

        visitation_matrix = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        final_size = 0

        for row_index in range(len(grid)):
            for col_index in range(len(grid[0])):
                element = grid[row_index][col_index]
                if element == 1 and not visitation_matrix[row_index][col_index]:
                    final_size = max(matrix_bfs(row_index, col_index), final_size)
        
        return final_size



        