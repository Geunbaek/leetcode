/**
 * @param {number[]} values
 * @return {number}
 */
var minScoreTriangulation = function(values) {
    const {length} = values;

    const memo = new Map();

    const dp = (i, j) => {
        if (i + 2 > j) {
            return 0;
        }

        if (i + 2 === j){
            return values[i] * values[i + 1] * values[j];
        }

        const key = i * length + j;
        if (!memo.has(key)) {
            let min = Infinity;
            for (let k = i + 1; k < j; k++) {
                min = Math.min(
                    min,
                    values[i] * values[k] * values[j] + dp(i, k) + dp(k, j)
                )
            }
            memo.set(key, min);
        }
        return memo.get(key);
    }
    return dp(0, length - 1);
};