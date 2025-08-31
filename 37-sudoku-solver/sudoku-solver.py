class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        from collections import defaultdict

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty = []

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    empty.append((r, c))
                else:
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[(r // 3) * 3 + (c // 3)].add(val)

        def backtrack(i=0):
            if i == len(empty):
                return True

            r, c = empty[i]
            b = (r // 3) * 3 + (c // 3)

            for ch in "123456789":
                if ch in rows[r] or ch in cols[c] or ch in boxes[b]:
                    continue

                board[r][c] = ch
                rows[r].add(ch)
                cols[c].add(ch)
                boxes[b].add(ch)

                if backtrack(i + 1):
                    return True

                board[r][c] = "."
                rows[r].remove(ch)
                cols[c].remove(ch)
                boxes[b].remove(ch)

            return False

        backtrack()
