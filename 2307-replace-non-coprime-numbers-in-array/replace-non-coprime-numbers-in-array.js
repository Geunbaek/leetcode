const gcd = (a, b) => {
    while (b > 0) {
        [a, b] = [b, a % b]; 
    }
    return a
}
const lcm = (a, b) => a * b / gcd(a, b)

const isCoprimes = (a, b) => gcd(a, b) <= 1

/**
 * @param {number[]} nums
 * @return {number[]}
 */
var replaceNonCoprimes = function(nums) {
    const stack = [];

    for (const num of nums) {
        let n = num;
        while (stack.length !== 0 && !isCoprimes(stack[stack.length - 1], n)) {
            n = lcm(stack.pop(), n);
        }

        stack.push(n);
    }
    return stack;
};