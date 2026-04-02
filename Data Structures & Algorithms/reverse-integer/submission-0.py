class Solution:
    def reverse(self, x: int) -> int:

        sign = -1 if x < 0 else 1

        
        newstr = str(abs(x))

        newstr = int(newstr[::-1]) * sign

        if newstr >= 2**31 - 1 or newstr <= -2**31:
            return 0
        else:
            return newstr
