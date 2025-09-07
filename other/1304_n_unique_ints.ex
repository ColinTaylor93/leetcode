defmodule Solution do
  @spec sum_zero(n :: integer) :: [integer]
  def sum_zero(n) do
    cond do
      rem(n, 2) == 1 ->
        [0 | build_pairs(n - 1)]

      true ->
        build_pairs(n)
    end
  end

  defp build_pairs(0), do: []

  defp build_pairs(n) do
    1..div(n, 2)
    |> Enum.flat_map(fn i -> [i, -i] end)
  end
end
