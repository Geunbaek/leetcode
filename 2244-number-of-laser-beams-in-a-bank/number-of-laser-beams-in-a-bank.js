/**
 * @param {string[]} bank
 * @return {number}
 */
var numberOfBeams = function(bank) {
    let answer = 0;
    let lastBeamCount = 0;

    for (const row of bank) {
        let beamCount = 0;

        for (const col of row) {
            if (col === "1") {
                beamCount += 1;
            }
        }

        answer += lastBeamCount * beamCount;

        if (beamCount > 0) {
            lastBeamCount = beamCount;
        }
    }

    return answer;
};