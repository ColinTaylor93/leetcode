public class KthLargest {
    // The `K`th largest element we that we look for
    private readonly int _k;

    // Min Heap for storing test scores
    private readonly PriorityQueue<int, int> _testScoresMinHeap;

    /**
    * Constructor, makes the min heap with the startings scores
    */
    public KthLargest(int k, int[] nums) {
        _k = k;
        _testScoresMinHeap = new PriorityQueue<int, int>();
        foreach (var n in nums)
            Add(n);
    }
    
    /**
    * Inserts a new value into the heap and returns the `K`th largest
    */
    public int Add(int val) {
        if (_testScoresMinHeap.Count < _k)
        {
            _testScoresMinHeap.Enqueue(val, val);
        }
        else if (val > _testScoresMinHeap.Peek())
        {
            _testScoresMinHeap.Dequeue();
            _testScoresMinHeap.Enqueue(val, val);
        }

        return _testScoresMinHeap.Peek();
    }
}

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest obj = new KthLargest(k, nums);
 * int param_1 = obj.Add(val);
 */