class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, n in enumerate(nums):
            if seen.get(target - n) != None:
                return [seen.get(target - n), i]
            seen[n] = i

        return [-1, -1]
        