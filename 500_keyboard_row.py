class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        # Get variables for letters from each row
        first_row = "qwertyuiop"
        second_row = "asdfghjkl"
        third_row = "zxcvbnm"

        return_list = []

        # go through each word an check what row the letter is from
        for word in words:
            first = second = third = False # flags for row with letter
            for char in word.lower():
                if char in first_row:
                    first = True
                if char in second_row:
                    second = True
                if char in third_row:
                    third = True

                # if 2 are True, move on
                if sum([first, second, third]) == 2:
                    continue

            # if we got through and only 1 flag is set add it to the return list
            if sum([first, second, third]) == 1:
                return_list.append(word)

        return return_list
