defmodule Solution do
  # Note: this fails with "Time linit exceeded

  @spec longest_palindrome(String.t()) :: String.t()
  def longest_palindrome(s) do
    len = String.length(s)
    if len < 2, do: s, else: do_longest_palindrome(s, len)
  end

  defp do_longest_palindrome(s, len) do
    chars = String.to_charlist(s)

    {start, max_len} =
      Enum.reduce(0..(len - 1), {0, 1}, fn i, {best_start, best_len} ->
        len1 = expand(chars, i, i)
        len2 = expand(chars, i, i + 1)
        current_max = max(len1, len2)

        if current_max > best_len do
          new_start = i - div(current_max - 1, 2)
          {new_start, current_max}
        else
          {best_start, best_len}
        end
      end)

    String.slice(s, start, max_len)
  end

  defp expand(chars, left, right), do: expand(chars, left, right, length(chars))

  defp expand(chars, left, right, len) do
    cond do
      left >= 0 and right < len and Enum.at(chars, left) == Enum.at(chars, right) ->
        expand(chars, left - 1, right + 1, len)

      true ->
        right - left - 1
    end
  end
end
