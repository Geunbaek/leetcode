/**
 * @param {number[][]} grid
 * @return {number}
 */
var minimumArea = function(grid) {
    const [r, c] = [grid.length, grid[0].length];

    let [sx, sy] = [c - 1, r - 1];
    let [nx, ny] = [0, 0];

    for (let y = 0; y < r; y++) {
        for (let x = 0; x < c; x++) {
            if (grid[y][x] === 1) {
                sx = Math.min(sx, x);
                sy = Math.min(sy, y);
                nx = Math.max(nx, x);
                ny = Math.max(ny, y);
            }
        }
    }

    console.log({sx, sy, nx, ny})
    return (ny - sy + 1) * (nx - sx + 1);
};