/**
 * @param {number} n
 * @return {boolean}
 */
var reorderedPowerOf2 = function(n) {
    function recur(path) {
        if (path.length >= length) {
            const result = parseInt(path.join(""));
            const log2Result = Math.log2(result);
            const isValid = Math.floor(log2Result) === log2Result;
            return isValid
        }

        for (let i = 0; i < 10; i ++) {
            if (counter[i] === 0) continue;
            if (path.length === 0 && i === 0) continue;
            counter[i] -= 1;
            const result = recur([...path, i]);
            if (result) return result
            counter[i] += 1;
        }
        return false
    }

    const numberStr = n.toString();
    const {length} = numberStr;
    const counter = new Array(10).fill(0);

    for (let i = 0; i < length; i ++) {
        counter[numberStr[i]] += 1;
    }
    return recur([]);
};
