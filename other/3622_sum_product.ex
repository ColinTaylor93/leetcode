defmodule Solution do
  @spec check_divisibility(n :: integer) :: boolean
  def check_divisibility(n) do
    sum = sum_digits(n)
    product = multiply_digits(n)
    total = sum + product

    rem(n, total) == 0
  end

  defp sum_digits(number) when is_integer(number) and number >= 0 do
    number
    |> Integer.digits()
    |> Enum.sum()
  end

  defp multiply_digits(number) when is_integer(number) and number >= 0 do
    number
    |> Integer.digits()
    |> Enum.product()
  end
end
