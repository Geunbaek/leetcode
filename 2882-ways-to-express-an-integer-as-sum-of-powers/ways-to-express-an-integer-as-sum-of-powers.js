/**
 * @param {number} n
 * @param {number} x
 * @return {number}
 */
var numberOfWays = function(n, x) {
    const dp = new Array(n + 1).fill(0);
    dp[0] = 1

    for(let i = 1; i <= n; i ++) {
        const value = i ** x;

        if (value > n) break;

        for (let j = n; j >= value; j--) {
            dp[j] = (dp[j] + dp[j - value]) % (10 ** 9 + 7)
        }
    }
    return dp[n]
};