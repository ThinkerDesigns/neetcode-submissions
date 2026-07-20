class Solution:
    def mySqrt(self, x: int) -> int:
        left = 1
        right = x
        middle = (left+right) // 2
        while left <= right:
            if (middle * middle) == x:
                return middle
            elif (middle * middle) >= x:
                right = middle - 1
                middle = (left+right) // 2
            elif (middle * middle) <= x:
                left = middle + 1
                middle = (left + right) // 2
        return middle