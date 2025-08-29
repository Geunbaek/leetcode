/**
 * @param {number[]} colors
 * @param {number[][]} queries
 * @return {number[]}
 */
var shortestDistanceColor = function(colors, queries) {
    const n = colors.length;

    const dp = [[], [], [], []]

    for (let i = 0; i < n; i ++) {
        const color = colors[i];
        dp[color].push(i);
    }

    const answer = [];
    for (const [index, color] of queries) {
        if (!dp[color].length) {
            answer.push(-1);
            continue;
        }

        let [left, right] = [0, dp[color].length - 1];

        while (left <= right) {
            const mid = Math.floor((left + right) / 2);
            if (dp[color][mid] <= index) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        if (0 <= left && left < dp[color].length && 0 <= right && right < dp[color].length) {
            const leftDiff = Math.abs(dp[color][left] - index)
            const rightDiff = Math.abs(dp[color][right] - index)
            const minDiff = Math.min(leftDiff, rightDiff);
            answer.push(minDiff)
        } else if (0 <= left && left < dp[color].length) {
            const leftDiff = Math.abs((dp[color][left] || 0) - index)
            answer.push(leftDiff)
        } else if (0 <= right && right < dp[color].length) {
            const rightDiff = Math.abs((dp[color][right] || n) - index)
            answer.push(rightDiff)
        } else {
            answer.push(-1)
        }
    }
    return answer
};