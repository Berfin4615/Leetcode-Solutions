class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        if n <= 1:
            return grid
        else:
            for r in range(n):
                i, j = r, 0
                tmp = []
                while i<n and j<n:
                    tmp.append(grid[i][j])
                    i +=1
                    j+=1
                tmp.sort(reverse=True)
                i, j, k = r, 0, 0
                while i < n and j < n:
                    grid[i][j] = tmp[k]
                    i += 1; j += 1; k += 1
            
            for c in range(1, n):
                i, j = 0, c
                tmp = []
                while i < n and j < n:
                    tmp.append(grid[i][j])
                    i += 1
                    j += 1
                tmp.sort()
                i, j, k = 0, c, 0
                while i < n and j < n:
                    grid[i][j] = tmp[k]
                    i += 1; j += 1; k += 1

            return grid