/**
 * @param {number[]} skill
 * @param {number[]} mana
 * @return {number}
 */
var minTime = function(skill, mana) {
    const n = skill.length, m = mana.length;
    let pref = new Array(n).fill(0);

    for (let i=1; i<n; i++) {
        pref[i] = pref[i - 1] + skill[i];
    }

    let tSum = skill[0] * mana[0];
   
    for (let j = 1; j < m; j++) {
        let tMax = skill[0] * mana[j];
        for (let i = 1; i < n; i++) {
            let tDiff = pref[i] * mana[j - 1] - pref[i - 1] * mana[j];
            if (tDiff > tMax) 
                tMax = tDiff;
        }
        tSum += tMax;
    }
    return tSum + pref[n - 1] * mana[m - 1];
};