class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            temiz = [x for x in row if x != "."]
            if len(set(temiz)) != len(temiz):
                return False
            if any(x not in "123456789" for x in temiz):
                return False

        for col in range(9):
            gorulen = set()
            for row in range(9):
                val = board[row][col]
                if val == ".":
                    continue
                if val not in "123456789" or val in gorulen:
                    return False
                gorulen.add(val)

        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                gorulen = set()
                for i in range(3):
                    for j in range(3):
                        val = board[box_row + i][box_col + j]
                        if val == ".":
                            continue
                        if val not in "123456789" or val in gorulen:
                            return False
                        gorulen.add(val)

        return True
