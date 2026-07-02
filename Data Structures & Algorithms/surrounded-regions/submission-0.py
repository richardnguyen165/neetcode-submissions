class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # Failed to realize that, if one square touches the border, than its not sorrounded
        # Use BFS
        
        ALL_MOVEMENTS = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visitation_matrix = [[False for _ in range(len(board[0]))] for _ in range(len(board))]
        
        def change_square(row, col):
            change = True
            all_squares = deque()
            all_squares.append([row, col])
            all_candidates = [[row, col]]
            
            while all_squares:
                current_row, current_col = all_squares.popleft()
                visitation_matrix[current_row][current_col] = True
                if (current_row == 0 or current_row == len(board) - 1) or (current_col == 0 or current_col == len(board[0]) - 1):
                    change = False
                for movement in ALL_MOVEMENTS:
                    if ((0 <= (current_row + movement[0]) < len(board)) and (0 <= current_col + movement[1] < len(board[0]))) and not visitation_matrix[current_row + movement[0]][current_col + movement[1]] and board[current_row + movement[0]][current_col + movement[1]] == "O":
                        all_squares.append([current_row + movement[0], current_col + movement[1]])
                        all_candidates.append([current_row + movement[0], current_col + movement[1]])
                        visitation_matrix[current_row + movement[0]][current_col + movement[1]] = True
            if change:
                for square in all_candidates:
                    board[square[0]][square[1]] = "X"


        for row_index in range(len(board)):
            for col_index in range(len(board[0])):
                element = board[row_index][col_index]
                if element == "O" and not visitation_matrix[row_index][col_index]:
                    change_square(row_index, col_index)
                visitation_matrix[row_index][col_index] = True