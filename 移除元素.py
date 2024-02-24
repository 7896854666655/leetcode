class Solution:

    '''
        采用双指针进行确定值
    '''

    def removeElement(self, nums: list[int], val: int) -> int:

        index1, index2 = 0, 0
        
        muns_len = len(nums)

        while index1 < muns_len:

            if nums[index1] == val:
            
                index1 += 1

            
            elif nums[index1] != val:

                nums[index2] = nums[index1]

                index1 += 1
                index2 += 1

        num = index2

        while index2 < muns_len:

            index2 += 1

            nums[index2] == 0

        return num
    
nums =[3,2,2,3]
val =3

print(Solution().removeElement(nums,val))
