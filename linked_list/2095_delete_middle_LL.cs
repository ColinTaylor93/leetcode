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
    public ListNode DeleteMiddle(ListNode head) {
        // Check for missing > 2 nodes to avoid System.NullReferenceException
        if (head == null || head.next == null) {
            return null;
        }

        ListNode slowPointer = head;
        ListNode fastPointer = head.next.next;

        // slow goes 1, fast goes 2 so
        // when fast is at the end slow will be in the middule
        while (fastPointer != null && fastPointer.next != null) {
            slowPointer = slowPointer.next;
            fastPointer = fastPointer.next.next;
        }

        // heave to remove the node and return head
        slowPointer.next = slowPointer.next.next;
        return head;
    }
}