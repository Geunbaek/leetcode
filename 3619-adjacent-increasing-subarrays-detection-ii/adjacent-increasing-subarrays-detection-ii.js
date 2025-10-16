
/**
 * @param {number[]} nums
 * @return {number}
 */
var maxIncreasingSubarrays = function(nums) {
    const n = nums.length;

    let count = 0;
    let prev_count = 0;
    let answer = 0;

    for (let i = 0; i < n; i++) {
        const prev = nums[i - 1];
        const now = nums[i];

        if (prev < now) {
            count += 1;
        } else {
            prev_count = count;
            count = 1;
        }

        answer = Math.max(answer, Math.min(prev_count, count));
        answer = Math.max(answer, Math.floor(count / 2));
    }
    return answer;
}; 