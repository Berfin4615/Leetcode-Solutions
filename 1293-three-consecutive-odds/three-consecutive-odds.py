class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        odd = 0
        if len(arr) < 3:
            return False
        for i in arr:
            if i%2 == 0:
                odd = 0
            else:
                odd += 1
                if odd == 3:
                    return True
                    break
        return False
