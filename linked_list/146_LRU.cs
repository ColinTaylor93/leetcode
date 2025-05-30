public class LRUCache {

    private Dictionary<int, LinkedListNode<(int key, int value)>> cache;
    private LinkedList<(int key, int value)> order;
    private int capacity;

    public LRUCache(int capacity) {
        this.capacity = capacity;
        this.cache = new Dictionary<int, LinkedListNode<(int key, int value)>>();
        this.order = new LinkedList<(int key, int value)>();
    }

    public int Get(int key) {
        if (!cache.ContainsKey(key)) return -1;
        var node = cache[key];
        order.Remove(node);
        order.AddLast(node);
        return node.Value.value;
    }

    public void Put(int key, int value) {
        if (cache.ContainsKey(key)) {
            var node = cache[key];
            order.Remove(node);
            node.Value = (key, value);
            order.AddLast(node);
        } else {
            if (cache.Count == capacity) {
                var lru = order.First.Value;
                order.RemoveFirst();
                cache.Remove(lru.key);
            }
            var newNode = new LinkedListNode<(int key, int value)>((key, value));
            order.AddLast(newNode);
            cache[key] = newNode;
        }
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.Get(key);
 * obj.Put(key,value);
 */