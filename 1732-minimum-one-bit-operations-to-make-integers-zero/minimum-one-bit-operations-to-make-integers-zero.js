/**
 * @param {number} n
 * @return {number}
 */
var minimumOneBitOperations = function(n) {
    if (n == 0) return 0;
    let i = 0;
    let num = 1;

    while (num * 2 <= n) {
        num *= 2;
        i += 1;
    }
    return 2 ** (i + 1) - 1 - minimumOneBitOperations(n ^ num);
};