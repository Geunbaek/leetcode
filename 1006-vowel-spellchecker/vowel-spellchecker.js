const removeVowel = (word) => {
    const vowels = new Set([...'aeiou']);
    return [...word].map(char => !vowels.has(char) ? char : ".").join("")
}

/**
 * @param {string[]} wordlist
 * @param {string[]} queries
 * @return {string[]}
 */
var spellchecker = function(wordlist, queries) {
    const wordMap = {}
    const lowerWordMap = {}
    const removedVowelWordMap = {}

    wordlist.forEach(word => {
        const lowerWord = word.toLowerCase()
        const removedVowelWord = removeVowel(lowerWord)
        wordMap[word] = word
        
        if (!(lowerWord in lowerWordMap)) {
            lowerWordMap[lowerWord] = word
        }

        if (!(removedVowelWord in removedVowelWordMap)) {
            removedVowelWordMap[removedVowelWord] = word
        }
    })
    return queries.map(query => {
        const lowerWord = query.toLowerCase()
        const removedVowelWord = removeVowel(lowerWord)
        if (query in wordMap) return wordMap[query];
        if (lowerWord in lowerWordMap) return lowerWordMap[lowerWord];
        if (removedVowelWord in removedVowelWordMap) return removedVowelWordMap[removedVowelWord];
        return ""
    })
};