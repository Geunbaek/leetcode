/**
 * @param {string} cell
 */
const isCell = (cell) => {
    const [alpha] = [...cell];
    return /[A-Z]/.test(alpha);
}

const parseCell = (cell) => {
    const [alpha, ...rest] = [...cell];
    const column = alpha.charCodeAt(0) - 'A'.charCodeAt(0);
    const row = parseInt(rest.join(''));
    return { row, column };
}

/**
 * @param {number} rows
 */
var Spreadsheet = function(rows) {
    this.table = Array.from({length: rows + 1}, () => new Array(26).fill(0))
};

/** 
 * @param {string} cell 
 * @param {number} value
 * @return {void}
 */
Spreadsheet.prototype.setCell = function(cell, value) {
    const {row, column} = parseCell(cell);
    this.table[row][column] = value;
};

/** 
 * @param {string} cell
 * @return {void}
 */
Spreadsheet.prototype.resetCell = function(cell) {
    const {row, column} = parseCell(cell);
    this.table[row][column] = 0;
};

Spreadsheet.prototype.getCell = function(cell) {
    const {row, column} = parseCell(cell);
    return this.table[row][column];
}

/** 
 * @param {string} formula
 * @return {number}
 */
Spreadsheet.prototype.getValue = function(formula) {
    const [l, r] = formula.slice(1).split("+");
    console.log({l, r})
    const left = isCell(l) ? this.getCell(l) : parseInt(l);
    const right = isCell(r) ? this.getCell(r) : parseInt(r);
    console.log({left, right})

    return left + right;
};

/** 
 * Your Spreadsheet object will be instantiated and called as such:
 * var obj = new Spreadsheet(rows)
 * obj.setCell(cell,value)
 * obj.resetCell(cell)
 * var param_3 = obj.getValue(formula)
 */