/**
 * @param {number[][]} points
 * @return {number}
 */
var countTrapezoids = function(points) {
    const cache = new Map();
    const MOD = 1_000_000_007n;

    let answer = 0n;
    let sum = 0n;

    for (const [, y] of points) {
        cache.set(y, (cache.get(y) || 0) + 1);
    }
    cache.forEach((value) => {
        const edge = (BigInt(value) * BigInt(value - 1)) / 2n;
        answer = (answer + edge * sum) % MOD;
        sum = (sum + edge) % MOD;
    })
    return Number(answer)
};