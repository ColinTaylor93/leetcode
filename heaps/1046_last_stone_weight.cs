public class Solution {
    public int LastStoneWeight(int[] stones) {
        // Create a priority queue (heap) with the stone, should be heaviest to lightest
        var stonesHeap = new PriorityQueue<int, int>();
        foreach (int stone in stones) {
            stonesHeap.Enqueue(stone, -stone);
        }

        while (stonesHeap.Count > 1) {
            // pop the top 2 items, subtract them, add to heap if needed
            int heaviest = stonesHeap.Dequeue();
            int secondHeaviest = stonesHeap.Dequeue();

            int diff = heaviest - secondHeaviest;
            if (diff > 0) {
                stonesHeap.Enqueue(diff, -diff);
            }
        }

        // return the leftover weights
        if (stonesHeap.Count == 1) {
            return stonesHeap.Dequeue();
        } else {
            return 0;
        }
    }
}