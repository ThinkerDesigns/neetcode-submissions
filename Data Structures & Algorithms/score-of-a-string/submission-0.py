class Solution:
    def scoreOfString(self, s: str) -> int:
        result = 0
        for x in range(len(s) - 1):
            result += abs(ord(s[x+1]) - ord(s[x]))
        return result