/**
 * @param {number} n
 * @param {number[][]} buildings
 * @return {number}
 */
var countCoveredBuildings = function(n, buildings) {
    const minRow = Array.from({length: n}, () => n + 1);
    const maxRow = Array.from({length: n}, () => 0);
    const minCol = Array.from({length: n}, () => n + 1);
    const maxCol = Array.from({length: n}, () => 0);

    for (const [x, y] of buildings) {
        minRow[x] = Math.min(minRow[x], y);
        maxRow[x] = Math.max(maxRow[x], y);
        minCol[y] = Math.min(minCol[y], x);
        maxCol[y] = Math.max(maxCol[y], x);
    }

    let answer = 0;

    for (const [x, y] of buildings) {
        if (minRow[x] < y && y < maxRow[x] && minCol[y] < x && x < maxCol[y]) {
            answer += 1;
        } 
    }
    return answer;
};  