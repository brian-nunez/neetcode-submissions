class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        highest = 0
        curr = 0

        for n in nums:
            if n == 1:
                curr += 1
                if curr > highest:
                    highest = curr
                continue
            curr = 0
        
        return highest
            

        