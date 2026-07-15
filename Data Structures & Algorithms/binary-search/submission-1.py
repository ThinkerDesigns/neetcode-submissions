class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        #print(middle)
        while left <= right:
            middle = (left + right)//2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                #left = middle
                left = middle + 1
            elif nums[middle] > target:
                #right = middle
                right = middle - 1
        return -1