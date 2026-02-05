/**
 * @param {number[]} nums
 * @return {number[]}
 */
var constructTransformedArray = function(nums) {
    return nums.map((num, i) => {
        const index = (i + num) % nums.length;
        return index < 0 ? nums[nums.length + index] : nums[index];
    })
};