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
 * @return {number[][]}
 */
var verticalTraversal = function(root) {
    const verticalInfo = new Map();
    let minLevel = Infinity;
    let maxLevel = -Infinity;
    const result = [];
    
    const dfs = (node, verticalLevel, horizontalLevel) => {
        if(!verticalInfo[verticalLevel]){
            verticalInfo[verticalLevel] = [];
        }
        minLevel = Math.min(minLevel, verticalLevel);
        maxLevel = Math.max(maxLevel, verticalLevel);
        if(node.left){
            dfs(node.left, verticalLevel - 1, horizontalLevel + 1);
        }
        verticalInfo[verticalLevel].push({value: node.val, horizontalLevel})
        if(node.right){
            dfs(node.right, verticalLevel + 1, horizontalLevel + 1);
        }
    }
    
    dfs(root, 0, 0);
    for(let verticalLevel = minLevel; verticalLevel <= maxLevel; verticalLevel ++){
        if(verticalInfo[verticalLevel]){
            const temp = [...verticalInfo[verticalLevel]]
            temp.sort((a, b) => a.horizontalLevel - b.horizontalLevel || a.value - b.value);
            result.push(temp.map(el => el.value));
        }
    }
    return result;
};