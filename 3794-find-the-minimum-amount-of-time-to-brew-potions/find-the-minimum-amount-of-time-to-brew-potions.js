/**
 * @param {number[]} skill
 * @param {number[]} mana
 * @return {number}
 */
var minTime = function(skill, mana) {
    const [r, c] = [mana.length, skill.length];

    const dp = Array.from({length: r}, () => new Array(c + 1).fill(0));
    const prefix = [0];

    for (let x = 0; x < c; x++) {
        prefix.push(prefix[prefix.length - 1] + skill[x]);
        dp[0][x + 1] = prefix.at(-1) * mana[0]
    }   
    for (let y = 1; y < r; y++) {
        let max = 0;
        const scale = mana[y];
        for (let x = 1; x <= c; x++) {
            const prev = dp[y - 1][x]
            const sum = (prefix[x - 1]) * scale;
            max = Math.max(max, prev - sum)
        }

        dp[y][0] = max;
        for (let x = 1; x <= c; x++) { 
            dp[y][x] = dp[y][x - 1] + (skill[x - 1] * scale)
        }

    }

    return dp[r - 1][c]
};
