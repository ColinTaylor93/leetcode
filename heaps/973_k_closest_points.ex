defmodule Solution do
  @spec k_closest(points :: [[integer]], k :: integer) :: [[integer]]
  def k_closest(points, k) do
    max_heap =
      points
      |> Enum.with_index()
      |> Enum.reduce(:gb_trees.empty(), fn {[x, y], index}, max_heap_acc ->
        # Squared distance to origin (no sqrt needed)
        distance_squared = x * x + y * y

        updated_max_heap =
          :gb_trees.enter(
            {-distance_squared, index, x, y},
            true,
            max_heap_acc
          )

        # Keep max_heap size <= k
        if :gb_trees.size(updated_max_heap) > k do
          {_removed_key, _removed_val, trimmed_max_heap} =
            :gb_trees.take_smallest(updated_max_heap)

          trimmed_max_heap
        else
          updated_max_heap
        end
      end)

    # Extract the k closest points
    max_heap
    |> :gb_trees.keys()
    |> Enum.map(fn {_neg_dist, _index, x, y} ->
      [x, y]
    end)
  end
end
