class Solution:
    def mySqrt(self, x: int) -> int:
        lo = 0
        hi = x
        while lo < hi:
            mid = (lo + hi) // 2
            if mid * mid <= x:
                lo = mid
            else:
                hi = mid
        return lo

x = 1000
print(Solution().mySqrt(x))