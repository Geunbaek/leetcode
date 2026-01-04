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
    const cache = new Map();
    let answer = 0;
    for (const num of nums)
    {
        if (cache.has(num))
        {
            const {count, sum} = cache.get(num);
            if (count === 4) answer += sum;
            continue;
        }
        const divisors = getDivisors(num);
        if (divisors.size === 4) {
            const sum = [...divisors].reduce((acc, cur) => acc + cur, 0);
            answer += sum;
            cache.set({count: divisors.size, sum});
        }
    }
    return answer;
};