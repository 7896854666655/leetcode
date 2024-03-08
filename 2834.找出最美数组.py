class Solution:
    def minimumPossibleSum(self, n: int, target: int) -> int:

        mod = 10**9 + 7

        if n <= target //2:
            return ((n * (1+n))//2) % mod
        
        else:
            return ((target//2)*(1+target//2)//2 + (n - target//2)*(target +target + (n - target//2) -1)//2)%mod

