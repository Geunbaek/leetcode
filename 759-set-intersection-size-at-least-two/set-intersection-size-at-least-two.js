/**
 * @param {number[][]} intervals
 * @return {number}
 */
var intersectionSizeTwo = function(intervals) {
    const n = intervals.length;
    const done = new Array(n).fill(2);
    intervals.sort((a, b) => a[0] - b[0] || b[1] - a[1]);
    let answer = 0;
    for (let i = n - 1; i >= 0; i--) {
        const [s, e] = intervals[i];
        const t = done[i];

        for (let num = s; num < s + t; num++) {
            for (let j = i - 1; j >= 0; j--) {
                const [s1, e1] = intervals[j];
                if (done[j] !== 0 && num <= e1) {
                    done[j] -= 1;
                }
            }
            answer += 1;
        }
    }
    return answer;
};