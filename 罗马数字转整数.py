class Solution:
    def romanToInt(self, s: str) -> int:
        
        I,V,X,L,C,D,M = 1,5,10,50,100,500,1000

        MAX = 0
        a = False
        i = 0
        
        while i<len(s):
                
                if a == True://当出现IV或者IX等将循环向前一步，添加a判断是否需要推前
                    i += 1
                    a = False

                if s[i] == "I":
                    if i == len(s)-2://防止超寨
                        if s[i+1] == "V":
                            MAX += 4
                            break

                        elif s[i+1] == "X":
                            MAX += 9 
                            break

                        else:
                            MAX += 1

                    
                    else:
                        MAX += 1

                elif s[i] == "V":
                    MAX += 5


                elif s[i] == "X":
                    if i == len(s)-1:
                        MAX += 10
                        break

                    if s[i+1] == "L":
                        a = True
                        MAX += 40
                        if i+1 == len(s)-1:
                            break

                    elif s[i+1] == "C":
                        a = True
                        MAX += 90 
                        if i+1 == len(s)-1:
                            break

                    else:
                        MAX += 10


                elif s[i] == "L":
                    MAX += 50


                elif s[i] == "C":

                    if i == len(s):
                        MAX += 100
                        break
                        
                    if s[i+1] == "D":
                        a = True
                        MAX += 400
                        if i+1 == len(s)-1:
                            break

                    elif s[i+1] == "M":
                        a = True
                        MAX += 900
                        if i+1 == len(s)-1:
                            break

                    else:
                        MAX += 100


                elif s[i] == "D":
                    MAX += 500


                elif s[i] == "M":
                    MAX += 1000

                i += 1 

        return MAX
    
s ="CXC"
print(Solution().romanToInt(s))
