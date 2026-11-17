class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # Solution, go through all the edges, and work them out from there

        # If you encounter an O at the edge, we need to traverse it so that we can mark that it is not sorrounded

        # Then go through the entire matrix again, and in the inner cells,
        # for those not visitied and O, flip to X

        VISITATION_MATRIX = [[False] * len(board[0]) for _ in range(len(board))]
        DIRECTIONS = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def in_bounds(r, c):
            return (0 <= r < len(board)) and (0 <= c < len(board[0]))

        def dfs_traversal(r, c):
            VISITATION_MATRIX[r][c] = True

            for direction in DIRECTIONS:
                r_i = direction[0]
                c_i = direction[1]
                if in_bounds(r + r_i, c + c_i) and not VISITATION_MATRIX[r + r_i][c + c_i] and board[r + r_i][c + c_i] == 'O':
                    dfs_traversal(r + r_i, c + c_i)


        # Step 1, go through all edge pieces

        for r in range(0, len(board)):
            if r == 0 or r == len(board) - 1:
                for c in range(0, len(board[0])):
                    if board[r][c] == 'O' and not VISITATION_MATRIX[r][c]:
                        dfs_traversal(r, c)
            else:
                if board[r][0] == 'O' and not VISITATION_MATRIX[r][0]:
                    dfs_traversal(r, 0)
                    
                if board[r][len(board[0]) - 1] == 'O' and not VISITATION_MATRIX[r][len(board[0]) - 1]:
                    dfs_traversal(r, len(board[0]) - 1)

        # Step 2: Go through the inner cells

        for r in range(1, len(board) - 1):
            for c in range(1, len(board[0]) - 1):
                if board[r][c] == 'O' and not VISITATION_MATRIX[r][c]: # It means the cell cannot be visited from the edges
                    board[r][c] = 'X'

