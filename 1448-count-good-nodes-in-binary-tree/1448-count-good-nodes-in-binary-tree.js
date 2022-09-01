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
var goodNodes = function(root) {
    let ans = 0;
    const dfs = (now, maxNum) => {
        if (now.val >= maxNum){
            ans += 1;
        }
        if (now.left){
            dfs(now.left, Math.max(maxNum, now.val));
        }
        if (now.right){
            dfs(now.right, Math.max(maxNum, now.val));
        }
    }
    dfs(root, -10000);
    return ans;
};