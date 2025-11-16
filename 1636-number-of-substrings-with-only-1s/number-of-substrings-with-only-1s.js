const sumRange = (n) => Math.floor(((n + 1) * n) / 2) 

/**
 * @param {string} s
 * @return {number}
 */
var numSub = function(s) {
    let answer = 0;
    let now = 0;
    const MOD = 1_000_000_007
    for (let i = 0; i < s.length; i++) {
        if (s[i] === '1') {
            now += 1;
        } else {
            answer += sumRange(now);
            answer %= MOD;
            now = 0;
        }
    }
    if (now) {
        answer += sumRange(now);
        answer %= MOD;
    }
    return answer;
};