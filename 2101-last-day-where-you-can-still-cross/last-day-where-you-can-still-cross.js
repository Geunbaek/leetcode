/**
 * @param {number} row
 * @param {number} col
 * @param {number[][]} cells
 * @return {number}
 */
var latestDayToCross = function(row, col, cells) {
    const find = (x) => {
        if (p[x] !== x) p[x] = find(p[x]);
        return p[x];
    }

    const union = (a, b) => {
        const ap = find(a);
        const bp = find(b);
        p[bp] = ap;
    }
    
    const n = row * col + 2;
    const board = Array.from({length: row}, () => Array.from({length: col}, () => 0));
    const p = Array.from({length:n}, (_, i) => i);

    const dx = [-1, -1, 0, 1, 1, 1, 0, -1];
    const dy = [0, 1, 1, 1, 0, -1, -1, -1];

    for (let i = 0; i < cells.length; i++) {
        const [y, x] = cells[i].map(num => num - 1);
        board[y][x] = 1;
        const now = (y * col) + x + 1; 
        for (let j = 0; j < 8; j++) {
            const nx = x + dx[j];
            const ny = y + dy[j];

            if (!(0 <= nx && nx < col && 0 <= ny && ny < row)) continue;
            if (board[ny][nx] === 0) continue;

            const neighbor = (ny * col) + nx + 1;

            union(now, neighbor)
        }
        if (x === 0) union(0, now)
        if (x === col - 1) union(n - 1, now) 
        if (find(0) === find(n - 1)) return i;
    }
};