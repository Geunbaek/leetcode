function isValidRange(start, end, target) {
    return start <= target && target < end;
}

/**
 * @param {number[][]} mat
 * @return {number[]}
 */
var findDiagonalOrder = function(mat) {
    const output = [mat[0][0]];
    const [r, c] = [mat.length, mat[0].length];
    
    const dx = [1, -1];
    const dy = [-1, 1];
    
    let [x, y] = [0, 0];
    let d = 0;

    while (x !== c - 1 || y !== r - 1) {
        const [nx, ny] = [x + dx[d], y + dy[d]];

        if (!isValidRange(0, c, nx) || !isValidRange(0, r, ny)) {
            if (d === 0) {
                if (!isValidRange(0, c, nx)) {
                    [x, y] = [x, y + 1];
                } else {
                    [x, y] = [x + 1, y]
                }
                d = 1;
            } else {
                if (!isValidRange(0, r, ny)) {
                    [x, y] = [x + 1, y];
                } else {
                    [x, y] = [x, y + 1];
                }
                d = 0;
            }
        } else {
            [x, y] = [nx, ny];
        }
        output.push(mat[y][x])
    }
    return output;
};