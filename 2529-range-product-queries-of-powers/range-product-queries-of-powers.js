/**
 * @param {number} n
 * @param {number[][]} queries
 * @return {number[]}
 */
var productQueries = function(n, queries) {
    const nums = [];

    let total = 0;
    for (let i = 30; i >= 0; i--) {
        const now = 1 << i;
        if (total + now <= n) {
            nums.push(now);
            total += now;
        }
    }
    
    const MOD = 1_000_000_007;
    const prefix = [1];
    for (let i = nums.length - 1; i >= 0; i--) {
        prefix.push((prefix.at(-1) * nums[i]));
    }
    
    console.log(prefix)
    const answer = [];
    for (const [l, r] of queries) {
        answer.push((prefix[r + 1] / prefix[l]) % MOD);
    }

    console.log()
    return answer;
};

