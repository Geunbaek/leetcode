/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {number[]} nums
 * @param {ListNode} head
 * @return {ListNode}
 */
var modifiedList = function(nums, head) {
    const numSet = new Set(nums);
    console.log({nums, head})
    let node = head;
    let prev = new ListNode(0, head);
    let ret = prev;
    while (node) {
        if (numSet.has(node.val)) {
            prev.next = node.next;
            node.next = null;
            node = prev.next;
        } else {
            prev = node;
            node = node.next;
        }
    }
    return ret.next;
};