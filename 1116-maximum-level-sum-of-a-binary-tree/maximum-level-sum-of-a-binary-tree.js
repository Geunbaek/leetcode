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
var maxLevelSum = function(root) {
    const cache = new Map();

    const dfs = (node, level) => {
        if (!node) return;
        cache.set(level, (cache.get(level) || 0) + node.val);
        dfs(node.left, level + 1);
        dfs(node.right, level + 1);
    } 

    dfs(root, 1);
    let minLevel = 10_001;
    let maxSum = -100_001;

    for (const [level, sum] of cache) {
        if (sum > maxSum) {
            minLevel = level;
            maxSum = sum;
            continue; 
        } 
        if (sum === maxSum && minLevel > level) {
            minLevel = level;
            maxSum = sum;
        }
    }
    return minLevel;
};