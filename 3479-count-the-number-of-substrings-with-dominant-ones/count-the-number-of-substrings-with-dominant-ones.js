/**
 * @param {string} s
 * @return {number}
 */
var numberOfSubstrings = function(s) {
    const prefix = [-1];

    for (let i = 0; i < s.length; i++) {
        if (i === 0 || s[i - 1] === "0") {
            prefix.push(i);
        } else {
            prefix.push(prefix[i]);
        }
    }

    let res = 0;
    for (let i = 1; i <= s.length; i++) {
        let cnt0 = s[i - 1] === "0" ? 1 : 0;
        let j = i;
        while (j > 0 && cnt0 * cnt0 <= s.length) {
            const cnt1 = i - prefix[j] - cnt0;
            if (cnt0 * cnt0 <= cnt1) {
                res += Math.min(j - prefix[j], cnt1 - cnt0 * cnt0 + 1);
            }
            j = prefix[j];
            cnt0++;
        }
    }
    return res;
};