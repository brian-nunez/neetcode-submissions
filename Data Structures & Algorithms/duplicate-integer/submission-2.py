# native time: O(n^2)
# native space: O(1)
# time: O(n)
# space: O(n)
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}

        for n in nums:
            if n in seen:
                return True
            seen[n] = True

        return False
