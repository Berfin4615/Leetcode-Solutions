class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True
        elif n <= 0:   
            return False
        else: 
            if n%4 == 0:
                x = math.log(n, 4)
                return x.is_integer()
            else:
                return False
        