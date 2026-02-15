defmodule Solution do
  @spec add_binary(a :: String.t, b :: String.t) :: String.t
  def add_binary(a, b) do
    # Make both strings the same length
    max_len = max(String.length(a), String.length(b))
    a = String.pad_leading(a, max_len, "0")
    b = String.pad_leading(b, max_len, "0")

    # step the numns up for right-to-left addition

    a_digits =
        String.graphemes(a)
        |> Enum.reverse()
    b_digits =
        String.graphemes(b)
        |> Enum.reverse()

    # add them together using carryover 1's
    {result, carry} =
      Enum.zip(a_digits, b_digits)
      |> Enum.reduce({[], 0}, fn {da, db}, {acc, carry} ->
        sum = String.to_integer(da) + String.to_integer(db) + carry

        case sum do
          0 -> {[ "0" | acc ], 0}
          1 -> {[ "1" | acc ], 0}
          2 -> {[ "0" | acc ], 1}
          3 -> {[ "1" | acc ], 1}
        end
      end)

    # incase of extra leftover, prepend a "1"
    result =
      if carry == 1 do
        ["1" | result]
      else
        result
      end

    # convert back to string and return
    Enum.join(result)
  end
end
