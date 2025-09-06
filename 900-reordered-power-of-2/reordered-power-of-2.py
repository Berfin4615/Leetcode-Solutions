class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        sig = Counter(str(n))
        if n == 2 or n == 1 or n == 4 or n == 8:
            return True
        for k in range(31):
            if Counter(str(1 << k)) == sig:
                return True
        return False