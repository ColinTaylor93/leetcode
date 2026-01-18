defmodule Solution do
  @spec least_interval(tasks :: [char], n :: integer) :: integer
  def least_interval(tasks, n) do
    # Count frequency of each task (A–Z)
    frequency =
      tasks
      |> Enum.frequencies()
      |> Map.values()

    # Find the maximum frequency
    max_frequency = Enum.max(frequency, fn -> 0 end)

    # Count how many tasks have the maximum frequency
    max_count =
      frequency
      |> Enum.count(&(&1 == max_frequency))

    # Calculate the result
    part_count = max_frequency - 1
    part_length = n + 1
    min_intervals = part_count * part_length + max_count

    max(length(tasks), min_intervals)
  end
end