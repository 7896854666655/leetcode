class Solution:

    
    def longestCommonPrefix(self, strs: list[str]) -> str:
        
        n = len( strs )

        str_len = len( strs[0] )

        strs_str = strs[0]

        for i,j in enumerate( strs ):
            if len(j) < str_len:
                str_len = len( j )
                strs_str = j

                i = str_len
                
                while i >= 0:
                    k = 0
                    
                    for v in range (0,n):
                        if strs_str[0:i] != strs[v][0:i]:
                            k = 1
                            break

                    i -= 1

                    if k == 0:
                        return strs_str[0:i]
                
                return ""
            
strs =["flower","flow","flight"]

print(Solution().longestCommonPrefix(strs))