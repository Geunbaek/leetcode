const getDivisors = (num) => {
    const divisors = new Set();

    for (let i = 1; i <= Math.ceil(Math.sqrt(num)); i++) {
        if (num % i === 0)
        {
            divisors.add(i);
            divisors.add(Math.floor(num / i));
        }
    }

    return divisors
}

/**
 * @param {number[]} nums
 * @return {number}
 */
var sumFourDivisors = function(nums) {
    let answer = 0;
    for (const num of nums)
    {
        const divisors = getDivisors(num);
        if (divisors.size === 4) {
            answer += [...divisors].reduce((acc, cur) => acc + cur, 0);
        }
    }
    return answer;
};