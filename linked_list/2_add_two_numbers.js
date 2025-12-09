/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(list1, list2) {
    const resultHead = new ListNode(0);
    let currentNode = resultHead;
    let carryOver = 0;

    while (list1 !== null || list2 !== null || carryOver !== 0) {
        const value1 = list1 !== null ? list1.val : 0;
        const value2 = list2 !== null ? list2.val : 0;

        const digitSum = value1 + value2 + carryOver;
        carryOver = Math.floor(digitSum / 10);
        const newDigit = digitSum % 10;

        currentNode.next = new ListNode(newDigit);
        currentNode = currentNode.next;

        if (list1 !== null) list1 = list1.next;
        if (list2 !== null) list2 = list2.next;
    }

    return resultHead.next;
};