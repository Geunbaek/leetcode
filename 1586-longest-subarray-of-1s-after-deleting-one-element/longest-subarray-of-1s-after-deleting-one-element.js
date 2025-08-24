/**
 * @param {number[]} nums
 * @return {number}
 */
var longestSubarray = function(nums) {
    const prefix = [0];

    for (const num of nums) {
        prefix.push(prefix[prefix.length - 1] + num);
    }

    let right = 1
    let max = 0;
    for (let left = 0; left < prefix.length; left ++) {
        while (right < prefix.length && prefix[right] - prefix[left] >= (right - left - 1)) {
            right += 1;
        }

        max = Math.max(max, right - left - 1);
    }
    return max - 1
};