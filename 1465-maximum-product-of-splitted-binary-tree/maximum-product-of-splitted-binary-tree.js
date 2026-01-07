/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number}
 */
var maxProduct = function(root) {
    const MAX = 50_001;
    const MOD = 1_000_000_007n;
    const memo = new Map()
    const dfs = (node) => {
        if (!node) return 0;
        let sum = node.val;
        sum += dfs(node.left);
        sum += dfs(node.right);
        memo.set(node, sum);
        return sum;
    }
    const total = dfs(root, 1);
    let maxProduct = 0n;

    for (const [key, value] of memo) {
        const now = BigInt(value) * BigInt(total - value);
        if (maxProduct < now) maxProduct = now;
    }

    return Number(maxProduct % MOD)
};