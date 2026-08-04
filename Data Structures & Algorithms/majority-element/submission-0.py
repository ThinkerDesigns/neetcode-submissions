class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}
        for x in nums:
            freq[x] = freq.get(x,0) + 1
        print(freq)
        return max(freq, key=freq.get)