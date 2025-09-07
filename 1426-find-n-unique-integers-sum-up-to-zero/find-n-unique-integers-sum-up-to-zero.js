/**
 * @param {number} n
 * @return {number[]}
 */
var sumZero = function(n) {
    const half = Math.floor(n / 2);
    const left = Array.from({length: n % 2 === 0 ? half : half + 1}, (_, i) => -(half - i));
    const right = Array.from({length: half}, (_, i) => i + 1);

    return [...left, ...right]
};