class Solution:


    def climbStairs(self, n: int) -> int:
        
        num_new, num_last = 1, 1
        num_new = 0

        if n == 1:
            return num_new
        else:
            for i in range ( n - 1 ):
                num_center = num_new
                num_new += num_new + num_last
                num_last = num_center
            
            return num_new




