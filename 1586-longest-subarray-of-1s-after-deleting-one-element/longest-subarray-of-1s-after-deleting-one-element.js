/**
 * @param {number[]} nums
 * @return {number}
 */
var longestSubarray = function(nums) {
    let left = 0;
    let zeros = 0;
    let ans = 0;

    for (let right = 0; right < nums.length; right++) {
        if (nums[right] === 0) zeros++;

        while (zeros > 1) {
            if (nums[left] === 0) zeros--;
            left++;
        }

        ans = Math.max(ans, (right - left + 1) - 1);
    }

    return ans < 0 ? 0 : ans; 
};