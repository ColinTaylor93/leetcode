/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
public class Solution {
    public ListNode RemoveNthFromEnd(ListNode head, int n) {
        if (head == null)
            return null;

        // find the length of the linked list
        int length = 0;
        ListNode p = head;
        while (p != null) {
            length++;
            p = p.next;
        }

        // get the index of the node to skip
        int skipIndex = length - n;

        // remake the linkedlist skipping the node we're removing
        ListNode newHead = null, newTail = null;
        p = head;
        int idx = 0;
        while (p != null) {
            if (idx != skipIndex) {
                // copy this node
                var node = new ListNode(p.val);
                if (newHead == null) {
                    newHead = node;
                    newTail = node;
                } else {
                    newTail.next = node;
                    newTail = node;
                }
            }
            p = p.next;
            idx++;
        }

        return newHead;
    }
}