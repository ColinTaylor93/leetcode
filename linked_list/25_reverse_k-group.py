# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        # Create a dummy node that points to the head of the list
        dummy_head = ListNode(0, head)
        group_prev = dummy_head

        while True:
            # Find the k-th node from group_prev (this marks the end of the group to reverse)
            kth_node = self.getKthNode(group_prev, k)
            if not kth_node:
                break  # If fewer than k nodes remain, no reversal needed

            group_next = kth_node.next  # The node following the current group

            # Reverse the group
            prev = group_next
            current = group_prev.next
            while current != group_next:
                next_temp = current.next  # Save next node
                current.next = prev       # Reverse the link
                prev = current            # Move prev forward
                current = next_temp       # Move current forward

            # Reconnect the reversed group with the previous part of the list
            temp = group_prev.next       # This is the tail after reversal
            group_prev.next = kth_node  # Connect previous part to new head
            group_prev = temp           # Move group_prev to the tail for next iteration

        return dummy_head.next

    def getKthNode(self, start_node, k):
        # Traverse k nodes ahead to find the k-th node
        while start_node and k > 0:
            start_node = start_node.next
            k -= 1
        return start_node