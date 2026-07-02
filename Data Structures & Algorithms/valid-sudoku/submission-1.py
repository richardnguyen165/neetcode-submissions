class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_storage = {
            0:  [],
            1:  [],
            2:  [],
            3:  [],
            4:  [],
            5:  [],
            6:  [],
            7:  [],
            8:  []
        }

        col_storage = {
            0:  [],
            1:  [],
            2:  [],
            3:  [],
            4:  [],
            5:  [],
            6:  [],
            7:  [],
            8:  []
        }

        square_storage = {
            0:  [],
            1:  [],
            2:  [],
            3:  [],
            4:  [],
            5:  [],
            6:  [],
            7:  [],
            8:  []
        }


        for row_index in range(9):
            for col_index in range(9):
                element = board[row_index][col_index]
                if element.isnumeric():
                    row_square = row_index // 3
                    col_square = col_index // 3
                    square_number = (row_square * 3) + col_square

                    if (element in row_storage.get(row_index)) or (element in col_storage.get(col_index)) or (element in square_storage.get(square_number)):
                        return False

                    print(square_storage)
                    row_storage[row_index].append(element)
                    col_storage[col_index].append(element)
                    square_storage[square_number].append(element)

        
        return True