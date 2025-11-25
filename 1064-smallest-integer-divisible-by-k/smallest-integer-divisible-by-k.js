/**
 * @param {number} k
 * @return {number}
 */
var smallestRepunitDivByK = function(k) {
    if (k % 2 === 0) return -1;
    let num = 0;
    let count = 1;
    const cache = new Set();
    while (1) {
        num += 1;
        if (num % k === 0) {
            return count;
        }
        if (cache.has(num)) {
            return -1;
        }
        count += 1;
        cache.add(num);
        num *= 10;
        num %= k;
    }
    return count;
};