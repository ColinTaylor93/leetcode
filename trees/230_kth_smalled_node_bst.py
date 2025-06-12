# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # create a list to store numbers
        num_list = []

        # helper function for DFS inorder adding to `num_list` so it will be sorted
        def depth_first_search(tree_node: Optional[TreeNode]):
            if not tree_node:
                return
            else:
                depth_first_search(tree_node.left)
                num_list.append(tree_node.val)
                depth_first_search(tree_node.right)

        # run the helper and return the k-1 element from the list
        depth_first_search(root)
        return num_list[k-1]