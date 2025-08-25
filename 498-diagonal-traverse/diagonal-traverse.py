class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if len(mat) == 1: 
            return mat[0]
        elif len(mat) == 0:
            return []
        else:
            m, n = len(mat), len(mat[0])
            diags = [[] for _ in range(m + n - 1)]
            for r, liste in enumerate(mat):
                for c in range(len(liste)):
                    diags[r + c].append(liste[c])
            reverse = False
            out = []
            for d in range(len(diags)):
                if reverse:
                    out.extend(diags[d])  
                else:
                    out.extend(reversed(diags[d])) 
                reverse = not reverse

            return out