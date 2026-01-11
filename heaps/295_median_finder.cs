using System;
using System.Collections.Generic;

/// <summary>
/// Class <c>MedianFinder</c> Keeps numbers and reports the median of them by having 2 heaps, 1 for lower half and 1 for higher half
/// Get the median hust peek lower half one or peek both and divide by 2
/// </summary>
public class MedianFinder
{
    // Max-heap (lower half)
    private PriorityQueue<int, int> left;
    
    // Min-heap (upper half)
    private PriorityQueue<int, int> right;

    public MedianFinder()
    {
        left = new PriorityQueue<int, int>();
        right = new PriorityQueue<int, int>();
    }

    public void AddNum(int num)
    {
        // Step 1: Add to max-heap (left)
        left.Enqueue(num, -num);

        // Step 2: Move the largest from left to right
        int moved = left.Dequeue();
        right.Enqueue(moved, moved);

        // Step 3: Balance sizes
        if (right.Count > left.Count)
        {
            int back = right.Dequeue();
            left.Enqueue(back, -back);
        }
    }

    public double FindMedian()
    {
        if (left.Count > right.Count)
        {
            return left.Peek();
        }

        return (left.Peek() + right.Peek()) / 2.0;
    }
}


/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder();
 * obj.AddNum(num);
 * double param_2 = obj.FindMedian();
 */