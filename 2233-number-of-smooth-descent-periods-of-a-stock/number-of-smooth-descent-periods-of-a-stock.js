/**
 * @param {number[]} prices
 * @return {number}
 */
var getDescentPeriods = function(prices) {
    const n = prices.length;
    const dp = Array.from({length: n}, () => 1);

    for (let i = 1; i < n; i++) {
        if (prices[i] - prices[i - 1] === -1) dp[i] += dp[i - 1];
    }
    return dp.reduce((acc, cur) => acc + cur, 0);
};