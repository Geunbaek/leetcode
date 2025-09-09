const MOD = 1_000_000_007

/**
 * @param {number} n
 * @param {number} delay
 * @param {number} forget
 * @return {number}
 */
var peopleAwareOfSecret = function(n, delay, forget) {
    const dp = new Array(n).fill(0);
    dp[0] = 1;

    let known = 0;

    for (let day = 1; day < n; day ++) {
        dp[day] = (known + dp.at(day - delay) - dp.at(day - forget) + MOD) % MOD;
        known = dp[day];
    }
    return dp
            .slice(n - forget, n)
            .reduce((acc, cur) => (acc + cur) % MOD, 0)
};