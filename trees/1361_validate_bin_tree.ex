defmodule Solution do
  @spec validate_binary_tree_nodes(n :: integer, left_child :: [integer], right_child :: [integer]) :: boolean
  def validate_binary_tree_nodes(n, left_child, right_child) do
    parents = :array.new(n, default: -1)

    case assign_parents(0, n, left_child, right_child, parents) do
      {:error, _} ->
        false

      {:ok, parents} ->
        # find root
        roots =
          for i <- 0..(n - 1),
              :array.get(i, parents) == -1,
              do: i

        if length(roots) != 1 do
          false
        else
          root = hd(roots)
          visited = MapSet.new()

          case dfs(root, left_child, right_child, visited) do
            {:ok, visited} -> MapSet.size(visited) == n
            :error -> false
          end
        end
    end
  end

  # Assign parents
  defp assign_parents(i, n, _left, _right, parents) when i == n do
    {:ok, parents}
  end

  defp assign_parents(i, n, left, right, parents) do
    parents =
      Enum.reduce([Enum.at(left, i), Enum.at(right, i)], parents, fn child, acc ->
        if child != -1 do
          if :array.get(child, acc) != -1 do
            throw(:multiple_parents)
          else
            :array.set(child, i, acc)
          end
        else
          acc
        end
      end)

    assign_parents(i + 1, n, left, right, parents)
  catch
    :multiple_parents -> {:error, :multiple_parents}
  end

  # DFS traversal
  defp dfs(-1, _left, _right, visited), do: {:ok, visited}

  defp dfs(node, left, right, visited) do
    if MapSet.member?(visited, node) do
      :error
    else
      visited = MapSet.put(visited, node)

      with {:ok, visited} <- dfs(Enum.at(left, node), left, right, visited),
           {:ok, visited} <- dfs(Enum.at(right, node), left, right, visited) do
        {:ok, visited}
      else
        _ -> :error
      end
    end
  end
end
