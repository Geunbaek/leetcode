/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function(digits) {
    const n = digits.length;
    for (let i = n - 1; i >= -1; i--) {
        
        if (i === -1) {
            digits.unshift(1);
            return digits;
        }

        const next = digits[i] + 1;
        if (next >= 10) digits[i] = 0;
        else {
            digits[i] = next;
            return digits;
        }
    }
    return digits;
};