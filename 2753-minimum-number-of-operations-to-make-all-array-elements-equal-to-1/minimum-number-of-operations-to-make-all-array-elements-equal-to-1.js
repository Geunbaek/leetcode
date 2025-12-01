const gcd = (a, b) => b === 0 ? a : gcd(b, a % b);


/**
 * @param {number[]} nums
 * @return {number}
 */
var minOperations = function(nums) {
    const n = nums.length;

    let num = 0;
    let g = 0;

    for (const x of nums) {
        if (x === 1) {
            num += 1;
        }
        g = gcd(g, x);
    }

    if (num > 0) {
        return n - num;
    }

    if (g > 1) {
        return -1;
    }
    let minLen = n;
    for (let i = 0; i < n; i++) {
        let currentGcd = 0;
        for (let j = i; j < n; j++) {
            currentGcd = gcd(currentGcd, nums[j]);
            if (currentGcd === 1) {
                minLen = Math.min(minLen, j - i + 1);
                break;
            }
        }
    }
    return minLen + n - 2;
};