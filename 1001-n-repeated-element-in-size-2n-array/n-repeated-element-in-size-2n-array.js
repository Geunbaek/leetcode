/**
 * @param {number[]} nums
 * @return {number}
 */
var repeatedNTimes = function(nums) {
    const dp = {};

    for (let i = 0; i < nums.length; i++) {
        if (nums[i] in dp) return nums[i];
        dp[nums[i]] = 1;
    }
};