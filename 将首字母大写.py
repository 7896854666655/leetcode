class Solution:
    def capitalizeTitle(self, title: str) -> str:
        
        a = title.split()
        
        a_len = len(a)

        i,j = 0, 0

        while i < a_len:

            a[i] = a[i].lower()
            a[i] = a[i].capitalize()
            i += 1
        
        return ' '.join(a)


            
a = "asds sdwcs asdwc asca safad"
print(Solution().capitalizeTitle(a))