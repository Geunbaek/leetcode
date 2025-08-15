/**
 * @param {number} n
 * @return {boolean}
 */
var isPowerOfFour = function(n) {
    if (n <= 0) return false

    while (n >= 4) {
        if (n % 4 !== 0) return false
        n /= 4
    }
    return n % 4 <= 1
};
// 10001

// 8 4 2 1 0