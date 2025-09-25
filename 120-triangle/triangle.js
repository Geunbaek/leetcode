/**
 * @param {number[][]} triangle
 * @return {number}
 */
var minimumTotal = function(triangle) {
    const height = triangle.length;

    for (let y = 1; y < height; y++) {
        const width = triangle[y].length;
        for (let x = 0; x < width; x++) {
            if (x === 0) {
                triangle[y][x] += triangle[y - 1][x];
            } else if (x === width - 1) {
                triangle[y][x] += triangle[y - 1][x - 1];
            } else {
                triangle[y][x] += Math.min(triangle[y - 1][x], triangle[y - 1][x - 1])
            }
        }
    }
    return Math.min(...triangle[height - 1]);
};