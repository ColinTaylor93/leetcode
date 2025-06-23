# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Create an empty dictionary to store value-to-index mappings
        indices = {}

        # Loop through the inorder list with index, map each value to its index
        for index, value in enumerate(inorder):
            indices[value] = index

        self.preorder_index = 0

        # Define recursive function to construct the binary tree
        def build_subtree(left: int, right: int) -> Optional['TreeNode']:
            # If there are no elements to construct the subtree
            if left > right:
                return None

            # Get the current root value and move to the next preorder index
            root_value = preorder[self.preorder_index]
            self.preorder_index += 1

            # Create the root node
            root = TreeNode(root_value)

            # Find the index of the root in inorder list
            mid = indices[root_value]

            # Recursively build the left and right subtrees
            root.left = build_subtree(left, mid - 1)
            root.right = build_subtree(mid + 1, right)

            return root

        # Finally, start building the tree from the full inorder range
        return build_subtree(0, len(inorder) - 1)