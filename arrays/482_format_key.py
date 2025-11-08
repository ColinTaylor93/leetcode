
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