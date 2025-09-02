var numberOfPairs = function (points) {
    let answer = 0;
    let n = points.length;
    
    for (let i = 0; i < n; i++) {
        const [ax, ay] = points[i];
        for (let j = 0; j < n; j++) {
            const [bx, by] = points[j];
            if (i === j) continue;
            if (!(ax <= bx && ay >= by)) continue;

            let illegal = false;

            for (let k = 0; k < n; k ++) { 
                if (i === k || j === k) continue
                const [cx, cy] = points[k];

                const isXContained = ax <= cx && cx <= bx;
                const isYContained = by <= cy && cy <= ay;

                illegal = isXContained && isYContained;

                if (illegal) {
                    break;
                }
            }

            if (!illegal) {
                answer++;
            }
        }
    }

    return answer;
};