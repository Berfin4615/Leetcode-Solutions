/**
 * @param {number[]} nums1
 * @param {number[]} nums2
 * @return {number}
 */

var findMedianSortedArrays = function(nums1, nums2) {
    let dummy = nums1.concat(nums2).sort((a, b) => a - b);
    let k = dummy.length;

    if (k % 2 === 0){
        let mid1 = k / 2 - 1;
        let mid2 = k / 2;
        return (dummy[mid1] + dummy[mid2]) / 2;
    } else {
        return dummy[Math.floor(k / 2)];
    }
};

