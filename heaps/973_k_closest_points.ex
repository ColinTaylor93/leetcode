defmodule Solution do
  @spec k_closest(points :: [[integer]], k :: integer) :: [[integer]]
  def k_closest(points, k) do
    min_heap =
      points
      |> Enum.with_index()
      |> Enum.reduce(:gb_trees.empty(), fn {[x, y], index}, min_heap_acc ->
        # Squared distance to origin (no sqrt needed)
        distance_squared = x * x + y * y

        updated_min_heap =
          :gb_trees.enter(
            {-distance_squared, index, x, y},
            true,
            min_heap_acc
          )

        # Keep min_heap size <= k
        if :gb_trees.size(updated_min_heap) > k do
          {_removed_key, _removed_val, trimmed_min_heap} =
            :gb_trees.take_smallest(updated_min_heap)

          trimmed_min_heap
        else
          updated_min_heap
        end
      end)

    # Extract the k closest points
    min_heap
    |> :gb_trees.keys()
    |> Enum.map(fn {_neg_dist, _index, x, y} ->
      [x, y]
    end)
  end
end
