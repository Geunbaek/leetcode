const getPattern = (depth, prev, visited, pattern, patternMap, ban) => {
    if (depth >= 3) {
        const patternStr = pattern.map(p => p.source).join("-");
        if (ban.has(patternStr)) return;
        ban.add(patternStr)
        patternMap.set(patternStr, (patternMap.get(patternStr) || 0) + 1);
        return;
    }

    for (let i = prev; i < visited.length; i++) {
        getPattern(depth + 1, i + 1, visited, [...pattern, visited[i]], patternMap, ban)
    }
}

/**
 * @param {string[]} username
 * @param {number[]} timestamp
 * @param {string[]} website
 * @return {string[]}
 */
var mostVisitedPattern = function(username, timestamp, website) {
    const userMap = new Map();
    
    const n = username.length;

    for (let i = 0; i < n; i ++) {
        const user = username[i];
        const time = timestamp[i];
        const source = website[i];

        if (!userMap.has(user)) {
            userMap.set(user, []);
        }

        userMap.get(user).push({time, source});
    }
    
    const patternMap = new Map();
    for (const [user, record] of userMap.entries()) {
        const ban = new Set();
        record.sort((a, b) => a.time - b.time)
        getPattern(0, 0, record, [], patternMap, ban);
    }

    console.log({userMap})
    const allPattens = [...patternMap.entries()].map(([p, c]) => ({p, c})).sort((a, b) => b.c - a.c || a.p.localeCompare(b.p))
    console.log({allPattens})
    return allPattens[0].p.split("-")
};