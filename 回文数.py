
class Solution:

    

    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        i,index = 0,1

        if len(s) == 2:
            if s[0] ==  s[1]:
                return True
            else:
                False

        for i in range(round(len(str(x))/2)-1):
            if s[i] == s[len(s)-1-i]:
                index = 1   
            else:
                index = 0
        return index 

x = 10
print(round(len(str(x))/2)-1)

print(Solution().isPalindrome(x))