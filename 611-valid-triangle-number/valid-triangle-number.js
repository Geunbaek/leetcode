const bs = (arr, l, r, target) => {
    let [left, right] = [l, r];

    while (left <= right) {
        const mid = Math.floor((left + right) / 2);
        if (arr[mid] >= target) {
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    } 

    return left
}



/**
 * @param {number[]} nums
 * @return {number}
 */
var triangleNumber = function(nums) {
    nums.sort((a, b) => a - b)
    const n = nums.length;
    let answer = 0;
    for (let a = 0; a < n; a++) {
        for (let b = a + 1; b < n; b++) {
            const bound = bs(nums, b + 1, n - 1, nums[a] + nums[b]);
            answer += bound - b - 1
        }
    }
    return answer
};
