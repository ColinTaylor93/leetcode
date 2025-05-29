# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Edge case — zero or one node
        if not head or not head.next:
            return head

        # Populate index → node mapping
        index_to_node = {}
        current_node = head
        node_index = 0
        while current_node:
            index_to_node[node_index] = current_node
            current_node = current_node.next
            node_index += 1
        total_nodes = node_index

        # Create a dummy pre-head to simplify appends
        dummy_head = ListNode(0)
        rebuild_tail = dummy_head

        # Walk through indices in steps of 2, rebuilding the list
        i = 0
        while i < total_nodes:
            # If at least two nodes remain, append them in swapped order
            if i + 1 < total_nodes:
                first_node  = index_to_node[i]
                second_node = index_to_node[i + 1]

                # append second_node, then first_node
                rebuild_tail.next = second_node
                rebuild_tail = rebuild_tail.next

                rebuild_tail.next = first_node
                rebuild_tail = rebuild_tail.next
            else:
                # Odd-length leftover: just append the final singleton
                rebuild_tail.next = index_to_node[i]
                rebuild_tail = rebuild_tail.next

            i += 2

        # Terminate the rebuilt list
        rebuild_tail.next = None
        return dummy_head.next