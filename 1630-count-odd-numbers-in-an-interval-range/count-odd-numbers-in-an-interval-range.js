/**
 * @param {number} low
 * @param {number} high
 * @return {number}
 */
var countOdds = function(low, high) {
    let count = high - low + 1;
    if (high % 2 === 0) count--;
    if (low % 2 === 0) count--;
    return Math.floor(count / 2) + 1;
};