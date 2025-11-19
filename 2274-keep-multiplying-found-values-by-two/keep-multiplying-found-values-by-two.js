/**
 * @param {number[]} nums
 * @param {number} original
 * @return {number}
 */
var findFinalValue = function(nums, original) {
    const cache = new Array(1001).fill(0);

    for (let i = 0; i < nums.length; i++) {
        if (nums[i] % original === 0 && Math.log2(nums[i] / original) === Math.floor(Math.log2(nums[i] / original))) {
            cache[Math.log2(nums[i] / original)] += 1;
        }
    }
    for (let i = 0; i < cache.length - 1; i++) {
        if (cache[i] !== 0 && cache[i + 1] === 0) return original * 2 ** (i + 1);
        if (cache[i] === 0) break;
    }

    return original;
};