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
 * @return {TreeNode}
 */
var subtreeWithAllDeepest = function(root) {
    const recur = (depth, node, parent) => {
        if (!node) return { depth, parent }
        
        const { depth: leftDepth, parent: leftParent } = recur(depth + 1, node.left, node);
        const { depth: rightDepth, parent: rightParent } = recur(depth + 1, node.right, node);
        if (leftDepth > rightDepth) return { depth: leftDepth, parent: leftParent };
        if (leftDepth < rightDepth) return { depth: rightDepth, parent: rightParent };
        return { depth: leftDepth, parent: node }
    }   

    const { depth, parent } = recur(0, root, null);
    return parent;
};