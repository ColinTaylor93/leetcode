public class Solution
{
    public IList<IList<int>> Subsets(int[] nums)
    {
        var result = new List<IList<int>>();
        Backtrack(0, new List<int>(), nums, result);
        return result;
    }

    /// <summary>
    /// Recursively builds all possible subsets using backtracking.
    /// </summary>
    private void Backtrack(int start, List<int> current, int[] nums, List<IList<int>> result)
    {
        result.Add(new List<int>(current));
        for (int i = start; i < nums.Length; i++)
        {
            current.Add(nums[i]);
            Backtrack(i + 1, current, nums, result);
            current.RemoveAt(current.Count - 1);
        }
    }
}
