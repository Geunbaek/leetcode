/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array}
 */
var chunk = function(arr, size) {
    const output = [];
    const {length} = arr;

    for (let i = 0; i < length; i += size) {
        output.push(arr.slice(i, i + size))
    }
    return output
};
