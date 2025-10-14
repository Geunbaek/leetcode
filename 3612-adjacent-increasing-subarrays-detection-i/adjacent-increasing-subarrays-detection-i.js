const isIncreased = (arr) => {
    let prev = arr[0];
    for (let i = 1; i < arr.length; i++) {
        const now = arr[i];
        if (now <= prev) {
            return false;
        }    
        prev = now;
    }
    return true;
}

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {boolean}
 */
var hasIncreasingSubarrays = function(nums, k) {
    const increasedRangeEndSet = new Set();

    for (let i = 0; i < nums.length; i++) {
        const range = nums.slice(i, i + k)
        if (range.length < k) break; 

        if (isIncreased(range)) {
            if (increasedRangeEndSet.has(i)) {
                return true;
            }
            increasedRangeEndSet.add(i + k);
        }
    }
    console.log(increasedRangeEndSet)
    return false;
};