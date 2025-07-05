/**
 * @param {number} n
 * @return {number}
 */
function lastRemaining(n) {
    const l = Math.floor(Math.log2(n));

    let answer = 1;

    for (let i = 0; i < l; i ++) {
        if (i % 2 === 0) {
            answer += Math.pow(2, i);
        } else {
            if (n % 2 !== 0) {
                answer += Math.pow(2, i);
            }
        }
        n = Math.floor(n / 2);
    }
    return answer
};