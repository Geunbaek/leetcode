/**
 * @param {Array} arr
 * @param {number} depth
 * @return {Array}
 */
var flat = function (arr, n) {
    const ret = [];
    for (let el of arr) {
        if (Array.isArray(el) && n !== 0) {
            ret.push(...flat(el, n - 1));
            continue
        }
        ret.push(el)
    }

    return ret
};