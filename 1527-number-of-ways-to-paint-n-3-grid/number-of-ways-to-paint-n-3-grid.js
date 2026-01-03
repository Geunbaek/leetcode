/**
 * @param {number} n
 * @return {number}
 */
var numOfWays = function(n) {
    let [x, y] = [6, 6];
    const MOD = 1_000_000_007;

    for (let i = 1; i < n; i++) {
        [x, y] = [((3 * x) + (2 * y)) % MOD, ((2 * x) + (2 * y))% MOD];
    } 

    return (x + y) % MOD;
};