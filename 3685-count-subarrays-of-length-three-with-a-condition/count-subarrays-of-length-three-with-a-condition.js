/**
 * @param {number[]} nums
 * @return {number}
 */
var countSubarrays = function(nums) {
    let count = 0;
    for(i=0; i+2<nums.length;i++){
        if(nums[i] + nums[i+2] === nums[i+1]/2){
            count += 1;
        } else {
            continue;
        }
    }
    return count;
};