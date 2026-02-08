public class Solution {
    public int[] TopKFrequent(int[] nums, int k) {
        // loop through nums and keep and a map for ints and their count
        Dictionary<int,int> counts = new Dictionary<int,int>();
        for (int i=0;i<nums.Length;i++) {
            if (counts.ContainsKey(nums[i])) {
                counts[nums[i]]++;
            } else {
                counts.Add(nums[i], 1);
            }
        }

        // sort the dictionary into a list
        List<int> sorted = counts.OrderByDescending(kv => kv.Value).Select(kv => kv.Key).ToList();

        // return the kth largest items
        return sorted.Take(k).ToArray();
    }
}