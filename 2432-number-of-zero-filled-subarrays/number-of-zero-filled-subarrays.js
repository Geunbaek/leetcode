

const sigma = (n) => ((n + 1) * n) / 2

/**
 * @param {number[]} nums
 * @return {number}
 */
var zeroFilledSubarray = function(nums) {
    const stack = []
    const zeros = []

    for (let num of nums) {
        if (num === 0) {
            stack.push(num);
        } else {
            let zero = 0;
            while (stack.length !== 0 && stack[stack.length - 1] === 0) {
                stack.pop();
                zero += 1;
            }

            if (zero) {
                zeros.push(zero);
            }
        }
    }

    let zero = 0;
    while (stack.length !== 0 && stack[stack.length - 1] === 0) {
        stack.pop();
        zero += 1;
    }

    if (zero) {
        zeros.push(zero);
    }
    return zeros.reduce((acc, zero) => acc + sigma(zero), 0);    
};

