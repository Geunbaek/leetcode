/**
 * @param {number[][]} grid
 * @return {number}
 */
var numMagicSquaresInside = function(grid) {
    const isMagicSquare = (x, y) => {
        let sum = -1;
        const numSet = new Set()
        for (let nx = x; nx < x + 3; nx++) {
            let colSum = 0;
            for (let ny = y; ny < y + 3; ny++) {
                if (!(1 <= grid[ny][nx] && grid[ny][nx] <= 9)) return false;
                if (numSet.has(grid[ny][nx])) return false;
                numSet.add(grid[ny][nx])
                colSum += grid[ny][nx];
            }
            if (sum === -1) sum = colSum;
            else if (sum !== colSum) return false;
        }

        for (let ny = y; ny < y + 1; ny++) {
            let rowSum = 0;
            for (let nx = x; nx < x + 3; nx++) {
                rowSum += grid[ny][nx];
            }
            if (sum === -1) sum = rowSum;
            else if (sum !== rowSum) return false;
        }

        let [nx, ny] = [x, y]
        let vSum = 0;
        for (let i = 0; i < 3; i++) {
            vSum += grid[ny + i][nx + i];
        }
        if (sum === -1) sum = vSum;
        else if (sum !== vSum) return false;

        [nx, ny] = [x, y + 2]
        vSum = 0;
        for (let i = 0; i < 3; i++) {
            vSum += grid[ny - i][nx + i];
        }
        if (sum === -1) sum = vSum;
        else if (sum !== vSum) return false;

        return true;
    }
    const [r, c] = [grid.length, grid[0].length];
    let answer = 0;
    for (let y = 0; y < r - 2; y++) {
        for (let x = 0; x < c - 2; x++) {
            if (isMagicSquare(x, y)) { console.log({x, y}); answer += 1;};
        }
    }
    return answer;
};