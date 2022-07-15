class Solution:
    def reverse(self, x: int) -> int:
        a = int(str(x)[::-1]) if x > 0 else -1*int(str(-1*x)[::-1])
        if a > 2147483647 or a < -2147483648: return 0
        return a
