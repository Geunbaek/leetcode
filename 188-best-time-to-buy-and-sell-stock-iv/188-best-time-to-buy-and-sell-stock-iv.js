/**
 * @param {number} k
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(k, prices) {
    
    const dp = Array.from({length: k + 1}, () => [0, -Infinity]);
    
    prices.forEach((price) => {
        for(let i = k; i > 0; i--){
            dp[i][0] = Math.max(dp[i][0], dp[i][1] + price);
            dp[i][1] = Math.max(dp[i][1], dp[i - 1][0] - price)
        }
    })

    return dp.at(-1)[0];
};