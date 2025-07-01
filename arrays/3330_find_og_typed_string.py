class Solution:
    def possibleStringCount(self, word: str) -> int:
        count = 1
        for index, char in enumerate(word):
            if index == 0:
                continue
            if word[index-1] == char:
                count += 1

        return count