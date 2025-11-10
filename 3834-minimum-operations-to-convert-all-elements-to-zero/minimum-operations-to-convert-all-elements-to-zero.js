/**
 * @param {number[]} nums
 * @return {number}
 */
var minOperations = function(nums) {
    const stack = [];
    let answer = 0;
    for (const num of nums) {
        while (stack.length !== 0 && stack.at(-1) > num){
            stack.pop();
        }

        if (num === 0) continue;
        if (stack.length === 0 || stack.at(-1) < num) {
            stack.push(num);
            answer += 1;
        }
    }
    return answer;
};