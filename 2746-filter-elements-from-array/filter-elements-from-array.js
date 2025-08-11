/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    const ret = [];
    const {length} = arr;

    for(let i = 0; i < length; i++) {
        if (fn(arr[i], i)) {
            ret.push(arr[i])
        }
    }

    return ret
};