/**
 * @param {number[]} nums
 * @param {Function} fn
 * @param {number} init
 * @return {number}
 */
var reduce = function(nums, fn, init) {
    let acc = init;
    const {length} = nums;

    for(let i = 0; i < length; i ++){
        acc = fn(acc, nums[i], i)
    }
    return acc;
};