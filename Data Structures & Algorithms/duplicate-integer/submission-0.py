class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        newDict ={}
        for x in range(len(nums)):
            if nums[x] not in newDict:
                newDict[nums[x]] = 1
            else:
                return True
        return False