/**
 * @param {number[]} nums
 * @param {number} value
 * @return {number}
 */
var findSmallestInteger = function(nums, value) {
    const numSet = Array.from({length: value + 1}, () => 0);

    for (const num of nums) {
        numSet[((num % value) + value) % value] += 1;
    }

    for (let i = 0; i <= nums.length; i++) {
        if (numSet[i % value] > 0) {
            numSet[i % value] -= 1;
            continue;
        }
        return i;
    }
};