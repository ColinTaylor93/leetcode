class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        c = r = o = a = k = 0
        max_frogs = 0
        active_frogs = 0
        
        for char in croakOfFrogs:
            if char == 'c':
                c += 1
                active_frogs += 1
                max_frogs = max(max_frogs, active_frogs) # Track highest concurrency
            elif char == 'r':
                r += 1
            elif char == 'o':
                o += 1
            elif char == 'a':
                a += 1
            elif char == 'k':
                k += 1
                active_frogs -= 1 # Frog is done, can be reused
            else:
                return -1 # Invalid character

            # A strict rule: we can't have a later letter appear more times than an earlier one
            if not (c >= r >= o >= a >= k):
                return -1

        # If everything finished cleanly, active_frogs will be 0 and counts will match
        if active_frogs == 0 and c == r == o == a == k:
            return max_frogs
            
        return -1