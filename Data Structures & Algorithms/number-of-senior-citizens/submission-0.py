class Solution:
    def countSeniors(self, details: List[str]) -> int:
        i = 0
        result = 0
        while i < len(details):
            if int(details[i][11:-2]) > 60:
                result += 1
            i += 1
        return result