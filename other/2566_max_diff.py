class Solution:
    def minMaxDifference(self, num: int) -> int:
        number_str = str(num)

        # Find the first digit (not last) that isn't '9'
        for index in range(len(number_str) - 1):
            if number_str[index] != '9':
                break
        else:
            # All digits up to the second-last are '9'
            index = len(number_str) - 1

        # Create the two modified versions
        max_version = number_str.replace(number_str[index], '9')
        min_version = number_str.replace(number_str[0], '0')

        return int(max_version) - int(min_version)