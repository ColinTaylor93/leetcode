class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        seen = set()
        dupes = []
        for num in nums:
            if num in seen:
                dupes.append(num)
            else:
                seen.add(num)
            
            if len(dupes) == 2:
                return dupes