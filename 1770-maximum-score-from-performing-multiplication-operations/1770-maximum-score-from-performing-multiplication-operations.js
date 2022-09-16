/**
 * @param {number[]} nums
 * @param {number[]} multipliers
 * @return {number}
 */
var maximumScore = function(nums, mults, st=0, en=nums.length-1, i=0, memo = new Map()) {
    if( st > en || i >= mults.length )
        return 0;
    
    var key = st + "," + en + ",";
    if( memo.has(key) ) return memo.get(key);
    
    let a = nums[st]*mults[i] + maximumScore(nums, mults, st+1, en, i+1, memo);
    let b = nums[en]*mults[i] + maximumScore(nums, mults, st, en-1, i+1, memo);
    
    let ans = Math.max(a,b);
    memo.set(key, ans);
    return ans;
};