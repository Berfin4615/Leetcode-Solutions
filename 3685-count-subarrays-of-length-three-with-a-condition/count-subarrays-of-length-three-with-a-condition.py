class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        count = 0
        i = 0
        while i + 2 < len(nums):
            if nums[i] + nums[i+2] == nums[i+1]/2:
                count += 1
                i += 1
            else:
                i += 1
        return count        