/**
 * @param {number[]} target
 * @return {number}
 */
var minNumberOperations = function(target) {
    let answer = 0;

    for (let i = 1; i < target.length; i++) {
        answer += Math.max(target[i] - target[i - 1], 0)
    }
    return answer + target[0];
};