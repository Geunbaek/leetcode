/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var kLengthApart = function(nums, k) {
    const stack = [];

    for (let i = 0; i < nums.length; i++) {
        if (nums[i] === 0) continue;
        if (stack.length !== 0 && i - stack[stack.length - 1] - 1 < k) return false;
        stack.push(i);
    }
    return true;
};