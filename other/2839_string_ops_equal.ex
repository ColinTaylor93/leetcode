defmodule Solution do
  @spec can_be_equal(s1 :: String.t, s2 :: String.t) :: boolean
  def can_be_equal(s1, s2) do
    s1 == s2 or
    s1 == swap_one_and_three(s2) or
    s1 == swap_two_and_four(s2) or
    s1 == swap_one_and_three(swap_two_and_four(s2))
  end

  def swap_one_and_three(string) do
    chars = String.split(string, "", trim: true)
    first  = Enum.at(chars, 0)
    second = Enum.at(chars, 1)
    third  = Enum.at(chars, 2)
    fourth = Enum.at(chars, 3)
    "#{third}#{second}#{first}#{fourth}"
  end

  def swap_two_and_four(string) do
    chars = String.split(string, "", trim: true)
    first  = Enum.at(chars, 0)
    second = Enum.at(chars, 1)
    third  = Enum.at(chars, 2)
    fourth = Enum.at(chars, 3)
    "#{first}#{fourth}#{third}#{second}"
  end
end
