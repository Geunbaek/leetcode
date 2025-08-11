/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    const ret = [];
    
    const {length} = arr;
    for (let i = 0; i < length; i ++) {
        ret.push(fn(arr[i], i));
    }

    return ret;
};