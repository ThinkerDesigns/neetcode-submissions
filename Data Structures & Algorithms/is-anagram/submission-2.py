class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq1 = {}
        for x in s:
            freq1[x] = freq1.get(x,0) + 1
        for x in t:
            freq1[x] = freq1.get(x,0) + 1
        for i in range(len(freq1)):
            if ((list(freq1.values())[i]) % 2 != 0) or (s[0] not in t):
                return False
        return True