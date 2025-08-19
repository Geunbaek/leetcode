

const sigma = (n) => ((n + 1) * n) / 2

/**
 * @param {number[]} nums
 * @return {number}
 */
var zeroFilledSubarray = function(nums) {
    let answer = 0;
    let zeros = 0;

    const {length} = nums; 
    for (let i = 0; i < length; i ++) {
        if (nums[i] === 0) {
            zeros += 1;
        } else {
            answer += ((zeros + 1) * zeros) / 2
            zeros = 0;
        }
    }
    answer += ((zeros + 1) * zeros) / 2
    return answer
};

