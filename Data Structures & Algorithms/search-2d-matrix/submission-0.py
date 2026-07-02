class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_length = len(matrix[0])
        matrix_length = len(matrix)

        low = 0
        high = (row_length * matrix_length) - 1

        while low <= high:
            midval = low + ((high - low) // 2)
            row_mid = midval // row_length
            col_mid = midval - (row_mid * row_length)
            print(midval, high, low, row_mid, col_mid)
            midval_value = matrix[row_mid][col_mid]
            if target < midval_value:
                high = midval - 1
            elif target > midval_value:
                low = midval + 1
            else:
                return True
        
        return False