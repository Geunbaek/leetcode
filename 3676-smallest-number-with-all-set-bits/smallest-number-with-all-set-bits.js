/**
 * @param {number} n
 * @return {number}
 */
var smallestNumber = function(n) {
    const binN = n.toString(2);
    return parseInt('1'.repeat(binN.length), 2);
};