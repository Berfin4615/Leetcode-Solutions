class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0
        for i in range(0, n):
            if 2**i == n:
                return True
            else:
                continue
        return False        