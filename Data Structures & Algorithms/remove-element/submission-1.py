class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        left = 0
        right = len(nums) - 1

        while left <= right:
            print(count, left, right, nums)
            if nums[left] == val:
                nums[left], nums[right] = nums[right], None
                right -= 1
            else:
                count += 1
                left += 1

        return count