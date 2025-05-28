"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        # make a hasmap to store values from the OG list
        original_nodes_map = { None: None }

        # 1st pass through the list to map the values
        current_node = head
        while current_node:
            copy = Node(current_node.val)
            original_nodes_map[current_node] = copy
            current_node = current_node.next

        # 2nd pass through to update the pointers for the random property
        current_node = head
        while current_node:
            # get the copy of the node, and remove the property
            copy = original_nodes_map[current_node]
            copy.next = original_nodes_map[current_node.next]
            copy.random = original_nodes_map[current_node.random]
            current_node = current_node.next

        return original_nodes_map[head]