/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
function maxSubsequence(nums, k) {
  return nums
           .map((num, index) => ({ index, num }))
           .sort((a, b) => b.num - a.num)
           .slice(0, k)
           .sort((a, b) => a.index - b.index)
           .map(el => el.num);
};