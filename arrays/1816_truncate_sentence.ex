defmodule Solution do
  @spec truncate_sentence(s :: String.t, k :: integer) :: String.t
  def truncate_sentence(s, k) do
    s
    |> String.split(" ")
    |> Enum.take(k)
    |> Enum.join(" ")
  end
end
