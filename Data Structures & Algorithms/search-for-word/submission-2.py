class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        '''
        Traversal direction top to bottom, left to right
        '''

        # Once we land on a word, we check its neighbours

        # First find the first letter of the word, and begin  backtracking on that letter

        # 4 possible neighbors

        def in_bound(row_pos, col_pos):
            return (0 <= row_pos <= len(board) - 1) and (0 <= col_pos <= len(board[0]) - 1)

        def find_word(all_seen, row_pos, col_pos, current_word):
            all_seen[row_pos][col_pos] = True

            if not current_word:
                return True
            
            result_one = False
            result_two = False
            result_three = False
            result_four = False

            if in_bound(row_pos - 1, col_pos) and current_word[0] == board[row_pos - 1][col_pos] and not all_seen[row_pos - 1][col_pos]:
                result_one = find_word(all_seen, row_pos - 1, col_pos, current_word[1:])
                all_seen[row_pos - 1][col_pos] = False
            if in_bound(row_pos + 1, col_pos) and current_word[0] == board[row_pos + 1][col_pos] and not all_seen[row_pos + 1][col_pos]:
                result_two = find_word(all_seen, row_pos + 1, col_pos, current_word[1:])
                all_seen[row_pos + 1][col_pos] = False
            if in_bound(row_pos, col_pos - 1) and current_word[0] == board[row_pos][col_pos - 1] and not all_seen[row_pos][col_pos - 1]:
                result_three = find_word(all_seen, row_pos, col_pos - 1, current_word[1:])
                all_seen[row_pos][col_pos - 1] = False
            if in_bound(row_pos, col_pos + 1) and current_word[0] == board[row_pos][col_pos + 1] and not all_seen[row_pos][col_pos + 1]:
                result_four = find_word(all_seen, row_pos, col_pos + 1, current_word[1:])
                all_seen[row_pos][col_pos + 1] = False
            
            return result_one or result_two or result_three or result_four

        current_matrix = [[False for _ in range(len(board[0]))] for _ in range(len(board))]

        result = False
        for row_number in range(0, len(board)):
            for col_number in range(0, len(board[0])):
                if board[row_number][col_number] == word[0]:
                    result = find_word(current_matrix, row_number, col_number, word[1:])
                    current_matrix[row_number][col_number] = False
                    if result:
                        return result

        return False