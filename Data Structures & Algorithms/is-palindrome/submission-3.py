class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        for x in s:
            if x.isdigit() == True:
                return False
        # got the variable below off of gemini :(
        cleaned = "".join(char for char in s if char.isalpha())
        print(cleaned)
        left = 0
        right = len(cleaned) - 1
        while left <= right:
            if cleaned[left] != cleaned[right]:
                return False
            left += 1
            right -= 1
        return True
