/**
 * @param {string[]} strs
 * @return {number}
 */
var minDeletionSize = function(strs) {
    const r = strs.length;
    const c = strs[0].length;
    let answer = 0;
    for (let x = 0; x < c; x++) {
        let isSorted = 0;
        for (let y = 1; y < r; y++) {
            if (strs[y][x] < strs[y - 1][x]) {
                isSorted = 1;
                break;
            }
        }
        answer += isSorted;
    }
    return answer;
};