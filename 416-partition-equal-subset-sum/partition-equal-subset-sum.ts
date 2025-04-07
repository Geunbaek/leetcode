
function canPartition(nums: number[]): boolean {
    const recur = (n: number, subSum: number) => {
        if (subSum === 0) return true;

        if (n === 0 || subSum < 0) return false;

        if (memo.has(`${n}-${subSum}`)) return memo.get(`${n}-${subSum}`)
        const result = recur(n - 1, subSum - nums[n - 1]) || recur(n - 1, subSum);
        // console.log(memo, result)
        memo.set(`${n}-${subSum}`, result);
        return result;
    }
    
    const n = nums.length;
    const total = nums.reduce((acc, num) => acc + num, 0);
    if (total % 2 !== 0) return false;
    const subSum = Math.floor(total / 2);
    const memo = new Map();
    return recur(n, subSum);
};