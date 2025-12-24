/**
 * @param {number[]} apple
 * @param {number[]} capacity
 * @return {number}
 */
var minimumBoxes = function(apple, capacity) {
    const n = capacity.length;
    const total = apple.reduce((acc, cur) => acc + cur, 0);
    capacity.sort((a, b) => b - a);

    let sum = 0;
    for (let i = 0; i < n; i++) {
        if (sum >= total) {
            return i;
        }
        sum += capacity[i];
    }
    return n
};