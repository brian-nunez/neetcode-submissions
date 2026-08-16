class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        length = len(nums)
        if length <= 0:
            return []
        ans = [None] * (length * 2)
        
        for i, n in enumerate(nums):
            ans[i] = n
            ans[i + length] = n

        return ans