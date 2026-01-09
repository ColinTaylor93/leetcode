# Definition for a binary tree node.
#
# defmodule TreeNode do
#   @type t :: %__MODULE__{
#           val: integer,
#           left: TreeNode.t() | nil,
#           right: TreeNode.t() | nil
#         }
#   defstruct val: 0, left: nil, right: nil
# end

defmodule Solution do
  @spec subtree_with_all_deepest(root :: TreeNode.t() | nil) :: TreeNode.t() | nil
  def subtree_with_all_deepest(root) do
    {node, _depth} = dfs(root)
    node
  end

  defp dfs(nil), do: {nil, 0}

  defp dfs(%TreeNode{} = node) do
    {left_node, left_depth} = dfs(node.left)
    {right_node, right_depth} = dfs(node.right)

    cond do
      left_depth > right_depth ->
        {left_node, left_depth + 1}

      right_depth > left_depth ->
        {right_node, right_depth + 1}

      true ->
        {node, left_depth + 1}
    end
  end
end
