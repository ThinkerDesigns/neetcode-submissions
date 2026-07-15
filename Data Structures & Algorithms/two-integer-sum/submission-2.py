class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for x in range(len(nums)):
            for i in range(len(nums)):
                if ((nums[x] + nums[i]) == target) and (len(result) < 2) and (x != i):
                    result.append(x)
                    result.append(i)
        return result