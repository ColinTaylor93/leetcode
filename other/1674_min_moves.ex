defmodule Solution do
  @spec min_moves(nums :: [integer], limit :: integer) :: integer
  def min_moves(nums, limit) do
    n = length(nums)
    max_sum = 2 * limit

    {first_half, second_half} = Enum.split(nums, div(n, 2))
    pairs = Enum.zip(first_half, Enum.reverse(second_half))

    diff_map =
      Enum.reduce(pairs, %{}, fn {v1, v2}, acc ->
        small = min(v1, v2)
        large = max(v1, v2)
        pair_sum = v1 + v2

        acc
        |> update_range(2, max_sum, 2)
        |> update_range(small + 1, large + limit, -1)
        |> update_range(pair_sum, pair_sum, -1)
      end)

    {_final_count, min_moves} =
      Enum.reduce(2..max_sum, {0, n}, fn target_sum, {running_count, min_so_far} ->
        new_count = running_count + Map.get(diff_map, target_sum, 0)
        {new_count, min(min_so_far, new_count)}
      end)

    min_moves
  end

  defp update_range(map, start_idx, end_idx, delta) do
    map
    |> Map.update(start_idx, delta, &(&1 + delta))
    |> Map.update(end_idx + 1, -delta, &(&1 - delta))
  end
end
