class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = float('inf')

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if abs(target - current_sum) < abs(target - closest):
                    closest = current_sum

                if current_sum == target:
                    return current_sum
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1

        return closest