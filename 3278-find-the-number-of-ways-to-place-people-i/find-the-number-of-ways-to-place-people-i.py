class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        count = 0
        n = len(points)

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                A = points[i]
                B = points[j]

                if A[0] <= B[0] and A[1] >= B[1]:  
                    obstructed = False
                    for k in range(n):
                        if k == i or k == j:
                            continue
                        C = points[k]
                        if A[0] <= C[0]  <= B[0]  and B[1] <= C[1] <= A[1]:
                            obstructed = True
                            break
                    if not obstructed:
                        count += 1

        return count
