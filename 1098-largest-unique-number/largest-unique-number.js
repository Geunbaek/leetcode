/**
 * @param {number[]} nums
 * @return {number}
 */
var largestUniqueNumber = function(nums) {
    const counter = nums.reduce((acc, num) => {
        const prev = acc[num] ?? 0;
        return {...acc, [num]: prev + 1};
    }, {})

    nums.sort((a, b) => b - a);

    for (const num of nums) {
        if (counter[num] === 1) return num;
    }

    return -1
};