const Counter = (arr) => {
    return arr.reduce((acc, cur) => {
        acc.set(cur, (acc.get(cur) || 0) + 1);
        return acc;
    }, new Map())
}

/**
 * @param {number[]} nums
 * @return {number}
 */
var maxFrequencyElements = function(nums) {
    const counter = Counter(nums);
    let _max = 0;
    for (const [key, value] of counter.entries()) {
        _max = Math.max(_max, value);
    }   

    let answer = 0;
    for (const [key, value] of counter.entries()) {
        if (value === _max) {
            answer += value;
        }
    } 
    
    return answer
};