class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        longest = 0
        first, second = 0, 0
        bestarea = 0
        for i in dimensions:
            length = sqrt(i[0] * i[0] + i[1] * i[1])
            area = i[0] * i[1]
            if length > longest or (length == longest and area > bestarea):
                longest = length
                bestarea = area
                first = i[0]
                second = i[1]
        return bestarea
