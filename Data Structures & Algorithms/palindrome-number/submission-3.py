class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        if "-" in x:
            return False
        elif len(x) == 1:
            return True
        left = 0
        right = len(x) - 1
        while left <= right:
            if x[left] != x[right]:
                print(left, right)
                return False
            left +=1
            right -= 1
        return True