/**
 * @param {number} n
 * @param {number[][]} connections
 * @return {number}
 */
var minimumCost = function(n, connections) {
    const find = (x) => {
        if (p[x] !== x) {
            p[x] = find(p[x]);
        }
        return p[x]
    }

    const union = (a, b) => {
        const ap = p[a];
        const bp = p[b];

        p[ap] = bp;
    }

    connections.sort((a, b) => a[2] - b[2]);

    const p = Array.from({length : n + 1}, (_, i) => i);
    let cost = 0;
    for (let i = 0; i < connections.length; i++) {
        const [u, v, c] = connections[i];

        if (find(u) !== find(v)) {
            cost += c;
            union(u, v);
        }
    }

    const area = new Set();

    for (let i = 1; i <= n; i++) {
        area.add(find(i))
    }
    return area.size === 1 ? cost : -1;
};