/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var maxSubarraySum = function(nums, k) {
    let prefix = 0;
    
    const kSum = Array.from({length: k}, () => Number.MAX_SAFE_INTEGER);
    kSum[k - 1] = 0;

    let answer = -Number.MAX_SAFE_INTEGER;
    for (let i = 0; i < nums.length; i++) {
        prefix += nums[i];
        answer = Math.max(answer, prefix - kSum[i % k]);
        kSum[i % k] = Math.min(kSum[i % k], prefix);
    }
    return answer;
};