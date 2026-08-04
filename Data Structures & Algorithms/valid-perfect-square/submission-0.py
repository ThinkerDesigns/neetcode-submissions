class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 0
        right = num
        middle = (left + right) // 2
        while left <= right:
            if (middle * middle) == num:
                return True
            elif (middle * middle) <= num:
                left = middle + 1
                middle = (left + right) // 2
            elif (middle * middle) >= num:
                right = middle - 1
                middle = (left + right) // 2
        return False