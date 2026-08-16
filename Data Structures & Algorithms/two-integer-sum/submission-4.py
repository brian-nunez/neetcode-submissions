class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for i, n in enumerate(nums):
            if seen.get(target - n) is not None:
                val = seen.get(target - n)
                if val is not None:
                    return [val, i]
            seen[n] = i

        return [-1, -1]
