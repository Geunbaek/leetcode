/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function(nums) {
    const n = nums.length;
    let bit = n;

    for (let i = 0; i < n; i ++) {
        bit ^= i ^ nums[i];
    }

    return bit
};