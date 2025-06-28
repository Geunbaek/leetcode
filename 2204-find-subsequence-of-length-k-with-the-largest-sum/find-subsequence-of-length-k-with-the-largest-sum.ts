function maxSubsequence(nums: number[], k: number): number[] {
  return nums
           .map((num, index) => ({ index, num }))
           .sort((a, b) => b.num - a.num)
           .slice(0, k)
           .sort((a, b) => a.index - b.index)
           .map(el => el.num);
};