/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function(nums) {
    const numSet = new Set(nums);

    for (let i = 0; i < 10001; i ++) {
        if (!numSet.has(i)) return i;
    }
};