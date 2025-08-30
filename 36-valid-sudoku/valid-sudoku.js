const isValidRow = (board, y) => {
    const numSet = new Set();
    for (let nx = 0; nx < 9; nx++) {
        if (board[y][nx] === ".") continue;
        if (numSet.has(board[y][nx])) return false;
        numSet.add(board[y][nx])
    }
    return true;
}

const isValidColumn = (board, x) => {
    const numSet = new Set();
    for (let ny = 0; ny < 9; ny++) {
        if (board[ny][x] === ".") continue;
        if (numSet.has(board[ny][x])) return false;
        numSet.add(board[ny][x])
    }
    return true;
}

const isValid3By3 = (board, x, y) => {
    const numSet = new Set();
    for (let ny = y; ny < y + 3; ny ++) {
        for (let nx = x; nx < x + 3; nx++) {
            if (board[ny][nx] === ".") continue;
            if (numSet.has(board[ny][nx])) return false;
            numSet.add(board[ny][nx])
        }
    }
    return true;
}

/**
 * @param {character[][]} board
 * @return {boolean}
 */
var isValidSudoku = function(board) {
    const n = 9;
    
    for (let y = 0; y < n; y += 3) {
        for (let x = 0; x < n; x+=3) {
            if (!isValid3By3(board, x, y)) return false;
        }
    }

    for (let y = 0; y < n; y++) {
        if (!isValidRow(board, y)) return false;
    }

    for (let x = 0; x < n; x ++) {
        if (!isValidColumn(board, x)) return false;
    }

    return true;
};