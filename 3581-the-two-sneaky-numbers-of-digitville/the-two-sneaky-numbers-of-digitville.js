/**
 * @param {number[]} nums
 * @return {number[]}
 */
var getSneakyNumbers = function(nums) {
    const numSet = new Set();
    return nums.reduce((acc, cur) => {
        if (!numSet.has(cur)) {
            numSet.add(cur);
            return acc;
        } else {
            return acc.concat([cur]);
        }
    }, [])
}