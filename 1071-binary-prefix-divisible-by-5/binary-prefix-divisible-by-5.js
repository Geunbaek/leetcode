/**
 * @param {number[]} nums
 * @return {boolean[]}
 */
var prefixesDivBy5 = function(nums) {
    return nums
            .reduce((acc, num) => {
                acc.now += BigInt(num);
                acc.answer.push(acc.now % BigInt(5) === BigInt(0));
                acc.now *= BigInt(2);
                return acc
            }, { now: BigInt(0), answer: [] })
            .answer;
};