/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const seen = {}; 

    for (let i = 0; i < nums.length; i++) {
        const current = nums[i];
        const complement = target - current;

        if (seen.hasOwnProperty(complement)) {
            return [seen[complement], i];
        }

        seen[current] = i;
    }
};