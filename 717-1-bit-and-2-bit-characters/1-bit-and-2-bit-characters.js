/**
 * @param {number[]} bits
 * @return {boolean}
 */
var isOneBitCharacter = function(bits) {
    const stack = []

    for (let i = 0; i < bits.length - 1; i++) {
        if (stack.length === 0) {
            if (bits[i] === 0) continue;
            stack.push(bits[i]);
            continue;
        }
        stack.pop();
    }
    return stack.length === 0 && bits[bits.length - 1] === 0;
};