/**
 * @param {number[]} nums
 * @return {number}
 */
var minimumOperations = function(nums) {
    return nums.reduce((acc, num) => {
        if (num % 3 === 0) return acc;
        return acc + Math.min(num % 3, 3 - num % 3);
    }, 0);
};