class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        integer = int("".join([str(x) for x in digits]))
        i = integer + 1 
        newArr = list(str(i))
        return [int(x) for x in newArr]