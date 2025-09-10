
const hasEqualEl = (arr1, arr2) => {
    return new Set(arr1).intersection(new Set(arr2)).size !== 0;
}

/**
 * @param {number} n
 * @param {number[][]} languages
 * @param {number[][]} friendships
 * @return {number}
 */
var minimumTeachings = function(n, languages, friendships) {
    const needConnectedSet = friendships.reduce((acc, [u, v]) => {
        if (!hasEqualEl(languages[u - 1], languages[v - 1])) {
            acc.add(u);
            acc.add(v);
        }
        return acc;
    }, new Set());

    const maxKnownLanguage = Array.from({length: n + 1}, () => new Set());
    let maxKnownLanguageCount = 0;
    for (const needConnected of needConnectedSet) {
        for (const language of languages[needConnected - 1]) {
            maxKnownLanguage[language].add(needConnected);
            maxKnownLanguageCount = Math.max(maxKnownLanguageCount, maxKnownLanguage[language].size);
        }
    }

    return needConnectedSet.size - maxKnownLanguageCount;
};