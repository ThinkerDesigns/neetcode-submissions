class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq1 = {}
        freq2 = {}
        for x in s:
            freq1[x] = freq1.get(x,0) + 1
        for x in t:
            freq1[x] = freq1.get(x,0) + 1
        for i in range(len(freq1)):
            if ((list(freq1.values())[i]) % 2 != 0) or (s[0] not in t):
                return False
        '''for x in t:
            freq2[x] = freq2.get(x,0) + 1
        for i in range(len(freq1)):
            if (list(freq1.values())[i]) != (list(freq2.values())[i]):
                print(list(freq1.values())[i], list(freq2.values())[i])
                return False
        '''
        return True