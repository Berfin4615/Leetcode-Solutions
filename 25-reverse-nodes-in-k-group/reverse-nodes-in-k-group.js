/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} k
 * @return {ListNode}
 */
var reverseKGroup = function(head, k) {
    let count = 0;
    let ptr = head;

    while (ptr && count < k) {
        ptr = ptr.next;
        count++;
    }

    if (count === k) {
        let prev = null;
        let curr = head;
        let next = null;
        let i = 0;

        while (i < k && curr) {
            next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
            i++;
        }
        head.next = reverseKGroup(next, k);

        return prev; 
    }
    return head;
};