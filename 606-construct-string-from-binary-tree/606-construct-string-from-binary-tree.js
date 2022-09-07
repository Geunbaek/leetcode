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
 * @return {string}
 */
var tree2str = function(root) {
    const dfs = (node) => {
        let answer = `${node.val}`;
        if(node.left){
            answer += `(${dfs(node.left)})`;
        }
        
        if(!node.left && node.right){
            answer += `()`;
        }
        
        if(node.right){
            answer += `(${dfs(node.right)})`;
        } 
        
        return answer;
    }
    return dfs(root);
};