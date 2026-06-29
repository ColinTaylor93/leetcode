defmodule Solution do
  @spec num_of_strings(patterns :: [String.t], word :: String.t) :: integer
  def num_of_strings(patterns, word) do
    patterns
    |> Enum.count(fn pattern -> String.contains?(word, pattern) end)
  end
end
