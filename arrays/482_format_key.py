
# This solution was really bad, only beat 5% of submissions.

class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        output = ""
        chars = []

        # Add all the characters in s that are not a dash to a list
        for char in s:
            if char != "-":
                chars.append(char.upper())

        
        # Build the result from the end of the list
        output_segments = []
        while chars:
            segment = ""
            # add the last k characters to output
            for i in range(k):
                if chars:
                    segment = chars.pop() + segment
            output_segments.insert(0, segment)

        # join segments with dashes
        output = "-".join(output_segments)
        return output

# Learned having `.insert(0, segment)` causes O(n^2) time complexity for each insertion
# and repeating string concatenation is also inefficient from line 22 (`segment = chars.pop() + segment`).
# new solution beats 53.73%, could be better still

class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        # Collect all valid characters (uppercase, no dashes)
        chars = [c.upper() for c in s if c != '-']
        
        output_segments = []
        i = len(chars)

        # Build segments from the end
        while i > 0:
            start = max(0, i - k)
            segment = ''.join(chars[start:i])
            output_segments.append(segment)
            i -= k

        # Reverse once at the end (instead of inserting at front)
        output_segments.reverse()

        return '-'.join(output_segments)