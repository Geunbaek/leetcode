const MOD = 10 ** 9 + 7;

/**
 * @param {number[][]} grid
 * @param {number} k
 * @return {number}
 */
var numberOfPaths = function(grid, k) {
    const [r, c] = [grid.length, grid[0].length];

    const dp = Array
                .from(
                    {length: r + 1}, 
                    () => Array.from(
                        {length: c + 1},
                        () => new Array(k).fill(0)
                    )
                )
    
    for (let y = 1; y <= r; y++) {
        for (let x = 1; x <= c; x++) {
            value = grid[y - 1][x - 1] % k;
            if (x == 1 && y == 1) {
                dp[y][x][value] = 1;
                continue;
            }
            for (let z = 0; z < k; z++) {
                const m = (z - value + k) % k;
                dp[y][x][z] = (
                    dp[y - 1][x][m] + dp[y][x - 1][m]
                ) % MOD;
            }
        }
    }
    return dp[r][c][0];
};