class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        integers = {}
        for x in range(len(nums)):
            if nums[x] not in integers:
                integers[nums[x]] = 1
            else:
                integers[nums[x]] += 1
        for i in range(len(integers)):
            if list(integers.values())[i] == 1:
                return list(integers)[i]
        