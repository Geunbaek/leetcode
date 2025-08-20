/**
 * @param {number[][]} matrix
 * @return {number}
 */
var countSquares = function(matrix) {
    const [r, c] = [matrix.length, matrix[0].length];
    const prefix = Array.from(
        {length: r + 1}, 
        () => Array.from(
            {length: c + 1}, 
            () => 0
        )
    );

    for (let y = 1; y <= r; y++) {
        for (let x = 1; x <= c; x++) {
            prefix[y][x] = prefix[y][x - 1] + matrix[y - 1][x - 1];
        }
    }

    for (let x = 1; x <= c; x++) {
        for (let y = 1; y <= r; y++) {
            prefix[y][x] = prefix[y - 1][x] + prefix[y][x]
        }
    }

    function getPrefixSum(x, y, size){
        if ((x + size >= c) || (y + size >= r)) return -1

        const [nx, ny] = [x + size, y + size];

        return prefix[ny + 1][nx + 1] - prefix[y][nx + 1] - prefix[ny + 1][x] + prefix[y][x];
    }

    let answer = 0;
    for (let y = 0; y < r; y++) {
        for (let x = 0; x < c; x++) {
            for (let size = 0; size <= Math.min(r - y, c - x); size++) {
                if (getPrefixSum(x, y, size) === (size + 1) * (size + 1)) {
                    answer += 1;
                } else {
                    break;
                }
            }
        }
    }
    return answer;
};