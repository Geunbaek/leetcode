/**
 * @param {number[]} nums
 * @return {number}
 */
var countValidSelections = function(nums) {
    const prefix = [0];

    for (const num of nums) {
        prefix.push(prefix.at(-1) + num);
    }
    let answer = 0;
    for (let i = 0; i < nums.length; i++) {
        if (nums[i] !== 0) continue;

        const prevSum = prefix[i + 1] - prefix[0];
        const nextSum = prefix[nums.length] - prefix[i + 1];
        
        if (Math.abs(prevSum - nextSum) === 1) answer += 1
        else if (prevSum === nextSum) answer += 2;
    }

    return answer;
};