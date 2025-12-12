const compare = (a, b) => {
    const aType = a[0] === "OFFLINE" ? 0 : 1;
    const bType = b[0] === "OFFLINE" ? 0 : 1;
    const aTime = Number(a[1]);
    const bTime = Number(b[1]);

    return aTime - bTime || aType - bType
}

/**
 * @param {number} numberOfUsers
 * @param {string[][]} events
 * @return {number[]}
 */
var countMentions = function(numberOfUsers, events) {
    const mentions = Array.from({length: numberOfUsers}, () => 0);
    const timestamps = Array.from({length: numberOfUsers}, () => -1);
    events.sort(compare)
    
    for (const [type, timestamp, ids] of events) {
        if (type === "MESSAGE") {
            if (ids === "ALL") {
                timestamps.forEach((_, i) => mentions[i]++);
            } else if (ids === "HERE") {
                timestamps.forEach((t, i) => (t === -1 || timestamp - t >= 60) && mentions[i]++);
            } else {
                ids.split(" ").forEach(id => mentions[Number(id.slice(2))]++);
            }
        } else if (type === "OFFLINE") {
            timestamps[ids] = Number(timestamp);
        }
    }
    return mentions
};