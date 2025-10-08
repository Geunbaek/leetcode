/**
 * @param {number[]} spells
 * @param {number[]} potions
 * @param {number} success
 * @return {number[]}
 */
var successfulPairs = function(spells, potions, success) {
    const [n, m] = [spells.length, potions.length];
    const answer = new Array(n).fill(0);

    const s = spells.map((spell, i) => ({spell, i})).sort((a, b) => b.spell - a.spell);
    potions.sort((a, b) => a - b);
    let l = 0;
    for (let r = 0; r < n; r++) {
        const spell = s[r].spell;

        while (l < m && potions[l] * spell < success) {
            l += 1;
        }
        answer[s[r].i] = (m - l)
    }

    return answer
};