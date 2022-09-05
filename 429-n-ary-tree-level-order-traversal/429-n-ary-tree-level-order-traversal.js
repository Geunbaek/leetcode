/**
 * // Definition for a Node.
 * function Node(val,children) {
 *    this.val = val;
 *    this.children = children;
 * };
 */

/**
 * @param {Node|null} root
 * @return {number[][]}
 */
var levelOrder = function(root) {
    const answer = [];
    if(!root){
        return answer
    }
    const levelMap = new Map();
    let maxDepth = 0;
    
    const dfs = (node, depth) => {
        if(!levelMap[depth]){
            levelMap[depth] = [];
        }
        maxDepth = Math.max(maxDepth, depth);
        levelMap[depth].push(node.val)
        node.children.forEach(child => {
            dfs(child, depth + 1);
        })
    }
    dfs(root, 0)
    for(let depth = 0; depth <= maxDepth; depth++){
        if(levelMap[depth]){
            answer.push(levelMap[depth]);
        }
    }
    return answer
};