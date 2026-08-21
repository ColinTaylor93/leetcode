# Soultion is AI assited since the original one I gave had a time limit issue.

defmodule Solution do
  @spec find_kth_smallest(coins :: [integer], k :: integer) :: integer
  def find_kth_smallest(coins, k) do
    # Filter out redundant coins (e.g. keep 2, drop 4)
    filtered = filter_coins(coins)

    # Binary search boundaries
    low = 1
    high = Enum.min(filtered) * k

    binary_search(low, high, k, filtered)
  end

  # Binary search for the smallest target number
  defp binary_search(low, high, k, coins) when low < high do
    mid = div(low + high, 2)

    if count_valid(mid, coins) >= k do
      binary_search(low, mid, k, coins)
    else
      binary_search(mid + 1, high, k, coins)
    end
  end

  defp binary_search(low, _high, _k, _coins), do: low

  # Counts how many multiples exist <= target using Inclusion-Exclusion
  defp count_valid(target, coins) do
    # Generate all non-empty subsets of coins
    subsets = get_subsets(coins)

    Enum.reduce(subsets, 0, fn subset, acc ->
      subset_lcm = Enum.reduce(subset, 1, &lcm/2)
      multiples = div(target, subset_lcm)

      # Odd size subsets add (+), even size subsets subtract (-)
      if rem(length(subset), 2) == 1 do
        acc + multiples
      else
        acc - multiples
      end
    end)
  end

  # Helper to remove coins that are multiples of smaller coins
  defp filter_coins(coins) do
    sorted = Enum.sort(coins)
    Enum.reduce(sorted, [], fn coin, acc ->
      if Enum.any?(acc, &(rem(coin, &1) == 0)), do: acc, else: [coin | acc]
    end)
  end

  # Helper to generate non-empty combinations of coins
  defp get_subsets([]), do: []
  defp get_subsets([head | tail]) do
    tail_subsets = get_subsets(tail)
    with_head = [[head] | Enum.map(tail_subsets, &[head | &1])]
    with_head ++ tail_subsets
  end

  # Math helpers
  defp gcd(a, 0), do: a
  defp gcd(a, b), do: gcd(b, rem(a, b))
  defp lcm(a, b), do: div(a * b, gcd(a, b))
end
