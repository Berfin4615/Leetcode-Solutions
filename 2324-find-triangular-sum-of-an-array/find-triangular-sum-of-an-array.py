class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        while len(nums) != 1:
            newNums = []
            for i in range(0, len(nums)-1):
                newNums.append((nums[i] + nums[i+1]) % 10)
            nums = newNums
        return nums[0]

        