class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        sig = Counter(str(n))
        for k in range(31):
            if Counter(str(1 << k)) == sig:
                return True
        return False