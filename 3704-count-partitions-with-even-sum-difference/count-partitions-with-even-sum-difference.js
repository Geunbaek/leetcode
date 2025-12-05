const sum = (arr) => arr.reduce((acc, cur) => acc + cur, 0);


/**
 * @param {number[]} nums
 * @return {number}
 */
var countPartitions = function(nums) {
    const n = nums.length;
    let [l, r] = [0, sum(nums)];

    let answer = 0;
    for (let i = 0; i < n - 1; i++) {
        l += nums[i];
        r -= nums[i];

        if (((l - r) % 2) === 0) answer += 1; 
    }
    return answer;
};