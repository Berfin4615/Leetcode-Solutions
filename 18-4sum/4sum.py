class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            min_sum_i = nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3]
            if min_sum_i > target:
                break  
            max_sum_i = nums[i] + nums[n - 1] + nums[n - 2] + nums[n - 3]
            if max_sum_i < target:
                continue  

            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                min_sum_j = nums[i] + nums[j] + nums[j + 1] + nums[j + 2]
                if min_sum_j > target:
                    break
                max_sum_j = nums[i] + nums[j] + nums[n - 1] + nums[n - 2]
                if max_sum_j < target:
                    continue

                l, r = j + 1, n - 1
                while l < r:
                    s = nums[i] + nums[j] + nums[l] + nums[r]
                    if s == target:
                        res.append([nums[i], nums[j], nums[l], nums[r]])

                        val_l = nums[l]
                        while l < r and nums[l] == val_l:
                            l += 1
                        val_r = nums[r]
                        while l < r and nums[r] == val_r:
                            r -= 1

                    elif s < target:
                        l += 1
                    else:
                        r -= 1

        return res
