/**
 * @param {number} n
 * @return {boolean}
 */
var reorderedPowerOf2 = function(n) {
    const getSortedNum = (num) => num.toString().split("").sort().join("");
    const target = getSortedNum(n);

    const poweredSet = new Set();

    for(let i = 0; i < 31; i++) {
        const poweredNum = 1 << i;
        poweredSet.add(getSortedNum(poweredNum));
    }

    return poweredSet.has(target)
};