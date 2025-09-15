const equal = (a) => (b) => {
    return a === b;
}

const longer = (size) => (nums) => {
    return nums.length > size;
}

/**
 * @param {number[]} nums
 * @param {number} target
 * @return {boolean}
 */
var isMajorityElement = function (nums, target) {
    return longer(nums.length / 2)(nums.filter(equal(target)))
}