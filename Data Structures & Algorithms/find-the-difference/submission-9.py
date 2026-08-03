class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        freq = {}
        for i in s:
            freq[i] = freq.get(i,0) + 1
        for i in t:
            if freq.get(i,0) == 0:
                return i
            freq[i] -= 1