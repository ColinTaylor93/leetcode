defmodule Solution do
  @spec sum_and_multiply(n :: integer) :: integer
  def sum_and_multiply(n) do
    digits = get_non_zero_digits(n)

    x = construct_x(digits)
    sum = Enum.sum(digits)

    x * sum
  end

  defp get_non_zero_digits(n) do
    n
    |> Integer.digits()
    |> Enum.filter(fn d -> d != 0 end)
  end

  defp construct_x([]), do: 0
  defp construct_x(digits), do: Integer.undigits(digits)
end
