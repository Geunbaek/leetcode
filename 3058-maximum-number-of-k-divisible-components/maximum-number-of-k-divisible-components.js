/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {number[]} values
 * @param {number} k
 * @return {number}
 */
var maxKDivisibleComponents = function(n, edges, values, k) {
    const graph = Array.from({length: n}, () => []);
    for (const [u, v] of edges) {
        graph[u].push(v);
        graph[v].push(u);
    }

    let answer = 0;
    const dfs = (node, parent) => {
        let sum = 0;

        for (const next of graph[node]) {
            if (next === parent) continue;
            sum += dfs(next, node);
            sum %= k;
        }

        sum += values[node];
        sum %= k;

        if (sum === 0) {
            answer += 1;
        }

        return sum;
    }
    dfs(0, -1);
    return answer;
};