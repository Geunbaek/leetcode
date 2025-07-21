/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    const counter = nums.reduce((acc, cur) => {
        const currentCount = (acc?.[cur] ?? 0) + 1
        const most = currentCount > (acc?.most?.count ?? 0) ? {
            count: currentCount,
            num: cur
        } : {
            count: acc?.most.count,
            num: acc?.most.num,
        }
        
        return {
            ...acc,
            [cur]: currentCount,
            most
        }
         
    }, {})
    return counter.most.num
};