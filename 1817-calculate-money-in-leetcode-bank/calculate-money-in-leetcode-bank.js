/**
 * @param {number} n
 * @return {number}
 */
var totalMoney = function(n) {
    return Array.from({length: n}, (_, i) => Math.floor(i / 7) + (i % 7) + 1).reduce((acc, cur) => acc + cur, 0)
};