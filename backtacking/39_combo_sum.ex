defmodule Solution do
  @spec combination_sum(candidates :: [integer], target :: integer) :: [[integer]]
  def combination_sum(candidates, target) do
    candidates
    |> Enum.sort()
    |> find_combinations(target, [])
  end

  defp find_combinations(_remaining_pool, 0, current_path), do: [current_path]

  defp find_combinations([], _target, _current_path), do: []

  defp find_combinations([next_val | _], target, _current_path) when next_val > target, do: []

  defp find_combinations([next_val | remaining_pool] = pool, target, current_path) do
    paths_including_val = find_combinations(pool, target - next_val, [next_val | current_path])
    paths_excluding_val = find_combinations(remaining_pool, target, current_path)
    paths_including_val ++ paths_excluding_val
  end
end