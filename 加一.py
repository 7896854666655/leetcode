class Solution:

    def plusOne(self, digits: list[int]) -> list[int]:

        num_room = {"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"0":0}

        index = len(digits)

        digits[index-1] = digits[index-1]+1

        if digits[index-1] == 10:

            if index == 1:

                digits.append(num_room["0"])

                digits[index-1] = 1

            elif index != 1:
                
                while index >= 1:

                    if index == 1:

                        digitss = [1,0]

                        i = 1

                        while i < len(digits):

                            digitss.append(digits[i])

                            i += 1

                        return digitss

                    digits[index-1] = 0

                    digits[index-2] += 1

                    if digits[index-2] == 10:

                        index -= 1
                    
                    else:

                        break
        else:                
            return digits
        
        return digits
    

digits =[9,9,9]
print(Solution().plusOne(digits))