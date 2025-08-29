class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        current = 0
        biggest = 0
        for i in range(0, len(nums)):
            for j in range(0, len(nums)):
                for k in range(0, len(nums)):
                    if i != j and j != k and i !=k and i < j < k:
                        current = (nums[i] - nums[j]) * nums[k]
                        if current > biggest:
                            biggest = current
                            print(i, j, k)
        return biggest
