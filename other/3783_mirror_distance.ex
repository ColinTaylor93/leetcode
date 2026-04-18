defmodule Solution do
  @spec mirror_distance(n :: integer) :: integer
  def mirror_distance(n) do
    abs(n - reverse(n))
  end

  defp reverse(n) when is_integer(n) do
    sign = if n < 0, do: -1, else: 1
    abs(n)
    |> Integer.to_string()
    |> String.reverse()
    |> String.to_integer()
    |> Kernel.*(sign)
  end
end
