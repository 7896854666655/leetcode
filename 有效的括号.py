class Solution:


    def isValid(self, s: str) -> bool:

        dic = {'{': '}',  '[': ']', '(': ')', '?': '?'}
        stack = ['?']

        for v in s:

            if v in dic: stack.append(c)

            elif dic[stack.pop()] != v: 
                return False 
            
        return len(stack) == 1

b = "()[]{"
c = "(]"
a = Solution().isValid(b)

print(a)
