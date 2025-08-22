defmodule Solution do
  @spec largest_number(nums :: [integer]) :: String.t
  def largest_number(nums) do
    nums
    |> Enum.map(&Integer.to_string/1)
    |> Enum.reduce([], &insert_in_stack/2)
    |> Enum.join("")
    |> normalize_result()
  end

  defp insert_in_stack(x, []), do: [x]

  defp insert_in_stack(x, stack) do
    {before, later} =
      Enum.split_while(stack, fn top ->
        top <> x >= x <> top
      end)

    before ++ [x] ++ later
  end

  @doc """
  Removes leading zeros for edge cases
  """
  defp normalize_result(result) do
    if String.starts_with?(result, "0"), do: "0", else: result
  end
end
