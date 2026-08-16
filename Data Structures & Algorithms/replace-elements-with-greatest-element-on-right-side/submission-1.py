class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        highest = arr[-1]
        right = len(arr) - 1


        for i in range(len(arr)-1, -1 , -1):
            item = arr[i]
            arr[i] = highest
            highest = max(item, highest)

        arr[-1] = -1
        return arr


            
        