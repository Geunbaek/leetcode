/**
 * @param {string} s1
 * @param {string} s2
 * @return {number}
 */
var minimumDeleteSum = function(s1, s2) {
    const dp = Array
                .from(
                    { length: s1.length + 1 }, 
                    () => Array.from({ length: s2.length + 1 }, () => ({ count: 0, path: [] })));

    for (let y = 1; y < s1.length + 1; y++) {
        for (let x = 1; x < s2.length + 1; x++) {
            if (s1[y - 1] === s2[x - 1]) {
                dp[y][x].count = dp[y - 1][x - 1].count + s1.charCodeAt(y - 1);
                dp[y][x].path = [...dp[y - 1][x - 1].path, s1[y - 1]];
                continue;
            } 

            if (dp[y - 1][x].count > dp[y][x - 1].count) {
                dp[y][x].count = dp[y - 1][x].count;
                dp[y][x].path = dp[y - 1][x].path;
            } else {
                dp[y][x].count = dp[y][x - 1].count;
                dp[y][x].path = dp[y][x - 1].path;
            }
        }
    }

    const s1Count = [...s1].reduce((acc, cur) => acc + cur.charCodeAt(0), 0);
    const s2Count = [...s2].reduce((acc, cur) => acc + cur.charCodeAt(0), 0);
    const total = s1Count + s2Count;

    return total - 2 * dp[s1.length][s2.length].count;
};