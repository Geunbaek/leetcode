const count = (arr) => {
    return arr
            .reduce((acc, cur) => {
                if (cur in acc) return ({...acc, [cur]: acc[cur] + 1});
                return ({...acc, [cur]: 1});
            }, {})
}

const compare = (a, b) => {
    return b[1] - a[1] || Number(b[0] - a[0]);
}

/**
 * @param {number[]} nums
 * @param {number} k
 * @param {number} x
 * @return {number[]}
 */
var findXSum = function(nums, k, x) {
    const n = nums.length;
    const answer = [];
    
    for (let i = 0; i < n; i++){
        if (i > n - k) break;
        const counter = count(nums.slice(i, i + k));
        const mostCommon = Object.entries(counter)
                                    .sort(compare)
                                    .slice(0, x)
                                    .reduce((acc, cur) => acc + Number(cur[0]) * cur[1], 0)
        answer.push(mostCommon)
    }
    return answer
};