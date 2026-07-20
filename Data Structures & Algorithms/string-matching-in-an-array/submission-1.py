class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        result = []
        for x in range(len(words)):
            for j in range(len(words)):
                if (words[x] in words[j]) and (words[x] != words[j]) and (words[x] not in result):
                    result.append(words[x])
        return result