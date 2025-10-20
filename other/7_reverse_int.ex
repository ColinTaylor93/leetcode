defmodule Solution do
  @int_max 2_147_483_647
  @int_min -2_147_483_648

  @spec reverse(x :: integer) :: integer
  def reverse(x) do
    sign = if x < 0, do: -1, else: 1
    digits =
    x
    |> abs()
    |> Integer.to_string()
    |> String.graphemes()

    # Treat list of digits as a stack — pop from end
    reversed_digits = Enum.reverse(digits)

    reversed_str = Enum.join(reversed_digits, "")
    reversed_int = String.to_integer(reversed_str) * sign

    if reversed_int < @int_min or reversed_int > @int_max do
    0
    else
    reversed_int
    end
  end
end
