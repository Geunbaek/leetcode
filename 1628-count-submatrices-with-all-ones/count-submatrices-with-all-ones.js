/**
 * @param {number[][]} mat
 * @return {number}
 */
var numSubmat = function(mat) {
    const n = mat[0].length;

    const heights = new Array(n).fill(0);
    let answer = 0;

    for (const row of mat) {
        for (let i = 0; i < n; i ++) {
            heights[i] = row[i] === 0 ? 0 : heights[i] + 1;
        }

        const stack = [{i: -1, cur: 0, h: -1}];

        for (let i = 0; i < n; i++) {
            const h = heights[i];
            while (stack.length && stack[stack.length - 1]["h"] >= h) {
                stack.pop();
            }
            
            const {i: j, cur: prev} = stack[stack.length - 1];
            const cur = prev + (i - j) * h

            stack.push({h, i, cur});
            answer += cur;
        }
    }
    return answer;
};