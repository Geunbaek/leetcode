/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var longestSubsequence = function(s, k) {
        let num = 0;
    let answer = 0;
    const bits = k.toString(2).length;

    for (let i = 0; i < s.length; i ++) {
        const c = s[s.length - i - 1];
        if (c === "1") {
            if (i < bits && num + (1 << i) <= k) {
                answer += 1;
                num += 1 << i;
            }
        } else {
            answer += 1;
        }
    }

    return answer
};