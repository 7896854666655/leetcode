class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        dict = {"0":0, "1":1}

        a_len, b_len = len(a), len(b)
        a_num, b_num = 0, 0
        i, j = 0, 0
        i_index, j_index = len(a)-1, len(b)-1
        
        while i < a_len:

            if a[i] == "0":
                
                i += 1

                i_index -= 1

                continue
            elif a[i] == "1":

                a_num += 2**i_index

                i_index -= 1

                i += 1
        
        while j < b_len:

            if b[j] == "0":
                
                j += 1

                j_index -= 1

                continue

            elif b[j] == "1":

                b_num += 2**j_index

                j_index -= 1

                j += 1

        num_max = a_num + b_num

        return bin(num_max).replace('0b','')
    
a = "1010"
b = "1011"
print(Solution().addBinary(a, b))

