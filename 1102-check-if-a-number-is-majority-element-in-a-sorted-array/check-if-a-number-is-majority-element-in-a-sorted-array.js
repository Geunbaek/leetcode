const equal = (a) => (b) => {
    return a === b;
}

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {boolean}
 */
var isMajorityElement = function (nums, target) {
    return nums
        .filter(equal(target))
        .length
        > (nums.length / 2)
};