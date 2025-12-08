/**
 * @param {number} n
 * @return {number}
 */
var countTriples = function(n) {
    const cache = new Set();
    let answer = 0;
    for (let i = 1; i <= n; i ++) {
        const pow = i * i;
        for (const num of cache) {
            if (cache.has(pow - num)) answer += 1;
        }
        cache.add(pow);
    }
    return answer;
};