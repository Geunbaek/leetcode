/**
 * @param {number[]} nums
 * @param {number[]} multipliers
 * @return {number}
 */
var maximumScore = function(nums, multipliers) {
    const [n, m] = [nums.length, multipliers.length];
    const dp = Array.from({length: m + 1}, () => Array(m + 1).fill(0));
    
    for(let i = m - 1; i >= 0; i --){
        for(let left = i; left >= 0; left--){
            const right = n - 1 - i + left
            dp[i][left] = Math.max(multipliers[i] * nums[left] + dp[i + 1][left + 1],
                                  multipliers[i] * nums[right] + dp[i + 1][left])
        }
    }
    return dp[0][0]
};
