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
    public ListNode MergeKLists(ListNode[] lists) {
        // create a list of nodes then sort them
        List<int> nodes = new List<int>();
        foreach (ListNode lst in lists) {
            ListNode curr = lst;
            while (curr != null) {
                nodes.Add(curr.val);
                curr = curr.next;
            }
        }
        nodes.Sort();

        // go through the sorted list and convert it to a linked list
        ListNode res = new ListNode(0);
        ListNode cur = res;
        foreach (int node in nodes) {
            cur.next = new ListNode(node);
            cur = cur.next;
        }
        return res.next;
    }
}