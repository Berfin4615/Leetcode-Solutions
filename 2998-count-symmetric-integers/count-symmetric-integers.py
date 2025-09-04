class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for i in range(low, high + 1):
            number = list(str(i))
            if len(number) % 2 != 0:
                continue
            else:
                seperate = int(len(number) / 2)
                left = 0
                right = 0
                for j in range(0, seperate):
                    left += int(number[j])
                for k in range(seperate, seperate*2):
                    right += int(number[k])
                if left == right:
                    count += 1
                else:
                    continue
        return count