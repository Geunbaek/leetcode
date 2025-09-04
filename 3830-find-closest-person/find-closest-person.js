/**
 * @param {number} x
 * @param {number} y
 * @param {number} z
 * @return {number}
 */
var findClosest = function(x, y, z) {
    const diff1 = Math.abs(z - x);
    const diff2 = Math.abs(z - y);

    if (diff1 === diff2) return 0

    return diff1 > diff2 ? 2 : 1
};