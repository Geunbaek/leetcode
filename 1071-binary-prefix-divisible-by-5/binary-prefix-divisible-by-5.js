/**
 * @param {number[]} nums
 * @return {boolean[]}
 */
var prefixesDivBy5 = function(nums) {
    return nums
            .reduce((acc, num) => {
                acc.now += num;
                acc.answer.push(acc.now % 5 === 0) ;
                acc.now *= 2;
                acc.now %= 5;
                return acc;
            }, { now: 0, answer: [] })
            .answer;
};