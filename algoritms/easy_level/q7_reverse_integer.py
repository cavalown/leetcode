"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
"""

class Solution:
    def reverse(self, x: int) -> int:
        if x < 2**32-1:
            y = list(str(abs(x)))
            y.reverse()
            y= int("".join(y))
            if y <2**31-1:
                if x >= 0:
                    return y
                else:
                    return y*(-1)
            return 0
        return 0

