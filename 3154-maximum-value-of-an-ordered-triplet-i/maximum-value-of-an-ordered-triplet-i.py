class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_val = 0
        max_i = nums[0]

        for j in range(1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                current = (max_i - nums[j]) * nums[k]
                max_val = max(max_val, current)
            max_i = max(max_i, nums[j])
        
        return max_val

